# 1752063
# Ngo Nguyen Duy An
"""
 * @author nhphung
"""
import functools

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self,partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def getName(self):
        return self.name

    @staticmethod
    def getSymbolFromFunction(decl):
        para = [x.varType for x in decl.param]
        return Symbol(decl.name.name, MType(para, decl.returnType))

    @staticmethod
    def getSymbolFromVarDecl(decl):
        return Symbol(decl.variable, decl.varType)

    @staticmethod
    def getSymbolFromDecl(decl):
        return Symbol.getSymbolFromFunction(decl) if type(decl) is FuncDecl else Symbol.getSymbolFromVarDecl(decl)


class CheckError:
    utils = Utils()

    @staticmethod
    def checkRedeclared(scope, symbol_list):
        new_scope = scope.copy()
        for x in symbol_list:
            f = CheckError.utils.lookup(x.name, new_scope, Symbol.getName)
            if f is not None:
                raise Redeclared(Function(), x.name) if type(x.mtype) is MType else Redeclared(Variable(), x.name)
            new_scope.append(x)
        return new_scope

    @staticmethod
    def checkMatchingParameter(pattern, current_para):
        if len(current_para) != len(pattern):
            return False
        return functools.reduce(lambda y, x: y and CheckError.checkMatchingType(x[0], x[1]),
                                zip(pattern, current_para), True)

    @staticmethod
    def checkMatchingType(patternType, paraType):
        if type(patternType) is ArrayPointerType:
            if type(paraType) in [ArrayType, ArrayPointerType] and type(patternType.eleType) is type(paraType.eleType):
                return True
        elif type(patternType) is FloatType:
            if type(paraType) in [IntType, FloatType]: return True
        elif type(patternType) is type(paraType):
            return True
        return False

    @staticmethod
    def checkReturnStmt(statement_list):
        # Check if statement list have break, continue, or return and return the first type that is not None
        for x in filter(lambda y: isinstance(y, list), statement_list):
            if x[0] is not None:
                return x[0]
        return None


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt", MType([], IntType())),
    Symbol("putIntLn", MType([IntType()], VoidType())),
    Symbol("putInt", MType([IntType()], VoidType())),
    Symbol("getFloat", MType([], FloatType())),
    Symbol("putFloat", MType([FloatType()], VoidType())),
    Symbol("putFloatLn", MType([FloatType()], VoidType())),
    Symbol("putBool", MType([BoolType()], VoidType())),
    Symbol("putBoolLn", MType([BoolType()], VoidType())),
    Symbol("putString", MType([StringType()], VoidType())),
    Symbol("putStringLn", MType([StringType()], VoidType())),
    Symbol("putLn", MType([], VoidType()))
    ]

    def __init__(self, ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        decl_list = CheckError.checkRedeclared(StaticChecker.global_envi, [Symbol.getSymbolFromDecl(x) for x in ast.decl])
        function_list = [x.name.name for x in filter(lambda x: type(x) is FuncDecl, ast.decl)] + [x.name for x in c]
        invoked_function = [x.name for x in c]
        res = self.lookup('main', decl_list, lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise NoEntryPoint()

        visit = [self.visit(decl, [decl_list, invoked_function]) for decl in ast.decl]
        function_list.remove('main')
        check_reachable = list(set(function_list) - set(invoked_function))
        if len(check_reachable) != 0:
            raise UnreachableFunction(check_reachable[0])
        return visit

    def visitFuncDecl(self, ast, c):
        try:
            para = CheckError.checkRedeclared([], [Symbol.getSymbolFromDecl(x) for x in ast.param])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        env = [para] + [[Symbol.getSymbolFromFunction(ast)] + c[0]]
        body_statement = []
        for decl in ast.body.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env)), env[1]]
            else:
                body_statement.append(self.visit(decl, (env, ast.returnType, False, ast.name.name, c[1])))
        stmt_type = CheckError.checkReturnStmt(body_statement)
        if type(ast.returnType) is not VoidType and type(stmt_type) is not Return:
            raise FunctionNotReturn(ast.name.name)
        return [Symbol.getSymbolFromFunction(ast)]

    def visitVarDecl(self, ast, c):
        return [Symbol.getSymbolFromVarDecl(ast)]

    def visitBlock(self, ast, c):
        ref_env, function_type, in_loop, function_name, invoked_function = c
        env = [[]] + ref_env
        statement_list = []
        for decl in ast.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env))] + env[1:]
            else:
                statement_list += [self.visit(decl, (env, function_type, in_loop, function_name, invoked_function))]
        return_type = CheckError.checkReturnStmt(statement_list)
        return [return_type]

    # Visit statement
    # Stmt_type break;: [Break()], continue;: [Continue()], return;: [Return()] else None
    def visitIf(self, ast, c):
        # If will return the type of then statement is then and else have same type else None because of 2 execute paths
        condition = self.visit(ast.expr, c)
        if type(condition) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt1 = [self.visit(ast.thenStmt, c)]
        then_type = CheckError.checkReturnStmt(stmt1)
        else_type = None
        if ast.elseStmt:
            stmt2 = [self.visit(ast.elseStmt, c)]
            else_type = CheckError.checkReturnStmt(stmt2)
        return [then_type] if type(then_type) is type(else_type) else [None]

    def visitDowhile(self, ast, c):
        # Do - while will return the type of list statement after do since we always have to execute that first
        ref_env, function_type, in_loop, function_name, invoked_function = c
        condition = self.visit(ast.exp, c)
        if type(condition) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt_list = functools.reduce(lambda y, x: y + [self.visit(x, (ref_env, function_type, True, function_name, invoked_function))], ast.sl, [])
        stmt_type = CheckError.checkReturnStmt(stmt_list)
        return [stmt_type] if type(stmt_type) is Return else [None]

    def visitFor(self, ast, c):
        # For will return [None] since we always have the path where we do not enter the for loop
        ref_env, function_type, in_loop, function_name, invoked_function = c
        condition1 = self.visit(ast.expr1, c)
        condition2 = self.visit(ast.expr2, c)
        condition3 = self.visit(ast.expr3, c)
        if type(condition1) is not IntType or type(condition3) is not IntType or type(condition2) is not BoolType:
            raise TypeMismatchInStatement(ast)
        loopStmts = [self.visit(ast.loop, (ref_env, function_type, True, function_name, invoked_function))]
        # loop_type = CheckError.checkReturnStmt(loopStmt)
        # return [loop_type] if type(loop_type) is Return else [None]
        return [None]

    def visitBreak(self, ast, c):
        ref_env, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise BreakNotInLoop()
        else:
            return [Break()]

    def visitContinue(self, ast, c):
        ref_env, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise ContinueNotInLoop()
        else:
            return [Continue()]

    def visitReturn(self, ast, c):
        ref_env, return_type, in_loop, function_name, invoked_function = c
        if ast.expr and type(return_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        expr_type = self.visit(ast.expr, c) if ast.expr else VoidType()
        if not CheckError.checkMatchingType(return_type, expr_type):
            raise TypeMismatchInStatement(ast)
        return [Return()]

    # Expression
    def visitBinaryOp(self, ast, c):
        op = ast.op
        lefths = self.visit(ast.left, c)
        righths = self.visit(ast.right, c)
        if op == '%':
            if type(lefths) is not IntType or type(righths) is not IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif op in ['+', '-', '*', '/']:
            if type(lefths) not in [IntType, FloatType] or type(righths) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return lefths if type(lefths) is type(righths) else FloatType()
        elif op in ['>', '>=', '<', '<=']:
            if type(lefths) not in [IntType, FloatType] or type(righths) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['==', '!=']:
            if type(lefths) is not type(righths) or type(lefths) not in [IntType, BoolType]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['&&', '||']:
            if type(lefths) is not BoolType or type(righths) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op == '=':
            if type(ast.left) not in [Id, ArrayCell]:
                raise NotLeftValue(ast)
            elif type(lefths)in [VoidType, ArrayPointerType, ArrayType]:
                raise TypeMismatchInExpression(ast)
            elif not CheckError.checkMatchingType(lefths, righths):
                raise TypeMismatchInExpression(ast)
            return lefths

    def visitUnaryOp(self, ast, c):
        exp_type = self.visit(ast.body, c)
        operator = ast.op
        if operator == '!':
            if type(exp_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
        else:
            if type(exp_type) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
        return exp_type

    def visitCallExpr(self, ast, c):
        ref_env, return_type, in_loop, function_name, invoked_function = c
        env = [x for y in ref_env for x in y]
        at = [self.visit(x, c) for x in ast.param]
        res = self.lookup(ast.method.name, env, lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
        elif not CheckError.checkMatchingParameter(res.mtype.partype, at):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != function_name and ast.method.name != 'main':
                invoked_function.append(ast.method.name)
            return res.mtype.rettype

    def visitArrayCell(self, ast, c):
        arrType = self.visit(ast.arr, c)
        idxType = self.visit(ast.idx, c)
        if type(arrType) not in [ArrayType, ArrayPointerType] or type(idxType) is not IntType:
            raise TypeMismatchInExpression(ast)
        return arrType.eleType

    def visitId(self, ast, c):
        scope = [x for y in c[0] for x in y]
        res = self.lookup(ast.name, scope, lambda x: x.name)
        if res is None or type(res.mtype) is MType:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype

    def visitIntType(self, ast, c):
        return IntType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBooleanType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()
