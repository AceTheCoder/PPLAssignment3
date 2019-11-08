
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
    def __init__(self, name, mtype, value=None, kind=Identifier()):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind

    def getName(self):
        return self.name

    @staticmethod
    def getSymbolFromFunction(decl):
        para = [x.varType for x in decl.param]
        return Symbol(decl.name.name, MType(para, decl.returnType), kind=Function())

    @staticmethod
    def getSymbolFromVarDecl(decl):
        return Symbol(decl.variable, decl.varType, kind=Variable())

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
                raise Redeclared(x.kind, x.name)
            new_scope.append(x)
        return new_scope

    @staticmethod
    def checkMatchingParameter(pattern, current_para):
        if len(current_para) != len(pattern):
            return False
        return all([CheckError.checkMatchingType(a, b) for (a, b) in zip(pattern, current_para)])

    @staticmethod
    def checkMatchingType(patternType, paraType):
        if type(patternType) is ArrayPointerType:
            if type(paraType) in [ArrayType, ArrayPointerType] and type(patternType.eleType) is type(paraType.eleType):
                return True
        else:
            if type(paraType) is type(patternType):
                return True
        return False

    @staticmethod
    def checkReturnStmt(statement_list):
        for x in statement_list:
            if isinstance(x, list):
                if type(x[1]) is not None:
                    return x[1]
        return None



class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt", MType([], IntType())),
    Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        function_list = [x.name.name for x in filter(lambda x: type(x) is FuncDecl, ast.decl)] + [x.name for x in c]
        visited_function = [x.name for x in c]
        decl_list = CheckError.checkRedeclared(StaticChecker.global_envi, [Symbol.getSymbolFromDecl(x) for x in ast.decl])
        res = self.lookup('main', decl_list, lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise NoEntryPoint()

        visit = [self.visit(decl, [decl_list, visited_function]) for decl in ast.decl]
        function_list.remove('main')
        check_reachable = list(set(function_list) - set(visited_function))
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
                body_statement += self.visit(decl, (env, ast.returnType, False, ast.name.name, c[1]))
        stmt_type = CheckError.checkReturnStmt(body_statement)
        if type(stmt_type) is not Return and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)
        return [Symbol.getSymbolFromFunction(ast)]

    def visitVarDecl(self, ast, c):
        return [Symbol.getSymbolFromVarDecl(ast)]

    def visitBlock(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        env = [[]] + scope
        statement_list = []
        for decl in ast.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env))] + env[::1]
            else:
                statement_list += self.visit(decl, (env, function_type, in_loop, function_name, invoked_function))
        return_type = CheckError.checkReturnStmt(statement_list)
        return [[ast, return_type]]

    # unfinished
    def visitIf(self, ast, c):
        condition = self.visit(ast.expr, c)
        if type(condition[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt1 = self.visit(ast.thenStmt, c)
        then_type = CheckError.checkReturnStmt(stmt1)
        else_type = None
        if ast.elseStmt is not None:
            stmt2 = self.visit(ast.elseStmt, c)
            else_type = CheckError.checkReturnStmt(stmt2)
        return [[ast, Return()]] if type(then_type) is type(else_type) and type(then_type) is Return else [[ast, None]]

    def visitDowhile(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        condition = self.visit(ast.exp, c)
        if type(condition[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt_list = functools.reduce(lambda y, x: y + self.visit(x, (scope, function_type, True, function_name, invoked_function)), ast.sl, [])
        stmt_type = CheckError.checkReturnStmt(stmt_list)
        return [[ast, stmt_type]] if type(stmt_type) is Return else [[ast, None]]

    def visitFor(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        condition1 = self.visit(ast.expr1, c)
        condition2 = self.visit(ast.expr2, c)
        condition3 = self.visit(ast.expr3, c)
        if type(condition1[0]) is not IntType or type(condition3[0]) is not IntType or type(condition2[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        loopStmt = self.visit(ast.loop, (scope, function_type, True, function_name, invoked_function))
        loop_type = CheckError.checkReturnStmt(loopStmt)
        return [[ast, loop_type]] if type(loop_type) is Return else [[ast, None]]

    def visitBreak(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise BreakNotInLoop()
        else:
            return [[ast, Break()]]

    def visitContinue(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise ContinueNotInLoop()
        else:
            return [[ast, Continue()]]

    def visitReturn(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        exprType = self.visit(ast.expr, c)[0] if ast.expr else VoidType()
        if not CheckError.checkMatchingType(return_type, exprType):
            raise TypeMismatchInStatement(ast)
        return [[ast, Return()]]

    # Expression
    def visitBinaryOp(self, ast, c):
        op = ast.op
        lefths = self.visit(ast.left, c)[0]
        left_type = type(lefths)
        righths = self.visit(ast.right, c)[0]
        right_type = type(righths)
        if op == '%':
            if left_type is not IntType or right_type is not IntType:
                raise TypeMismatchInExpression(ast)
            return [IntType()]
        elif op in ['+', '-', '*', '/']:
            if left_type not in [IntType, FloatType] or right_type not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return [lefths] if left_type is right_type else [FloatType()]
        elif op in ['>', '>=', '<', '<=']:
            if left_type not in [IntType, FloatType] or right_type not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op in ['==', '!=']:
            if left_type is not right_type or left_type not in [IntType, BoolType]:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op in ['&&', '||']:
            if left_type is not BoolType or right_type is not BoolType:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op == '=':
            if type(ast.left) not in [Id, ArrayCell]:
                raise NotLeftValue(ast)
            if left_type in [VoidType, ArrayPointerType, ArrayType]:
                raise TypeMismatchInExpression(ast)
            elif left_type is not FloatType:
                if right_type is not left_type:
                    raise TypeMismatchInExpression(ast)
            else:
                if right_type not in [FloatType, IntType]:
                    raise TypeMismatchInExpression(ast)
            return [lefths]

    def visitUnaryOp(self, ast, c):
        exp = self.visit(ast.body, c)
        expType = type(exp[0])
        operator = ast.op
        if operator == '!':
            if expType is not BoolType:
                raise TypeMismatchInExpression(ast)
        else:
            if expType not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
        return [exp[0]]

    def visitCallExpr(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        env = [x for y in scope for x in y]
        at = [self.visit(x, (scope, None, in_loop, function_name, invoked_function))[0] for x in ast.param]
        res = self.lookup(ast.method.name, env, lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
        elif not CheckError.checkMatchingParameter(res.mtype.partype, at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != function_name and ast.method.name != 'main':
                invoked_function.append(ast.method.name)
            return [res.mtype.rettype]

    def visitArrayCell(self, ast, c):
        arrType = self.visit(ast.arr, c)
        idxType = self.visit(ast.idx, c)
        if type(arrType[0]) not in [ArrayType, ArrayPointerType] or type(idxType[0]) is not IntType:
            raise TypeMismatchInExpression(ast)
        return [arrType[0].eleType]

    def visitId(self, ast, c):
        scope = [x for y in c[0] for x in y]
        res = self.lookup(ast.name, scope, lambda x: x.name)
        if res is None or type(res.mtype) is MType:
            raise Undeclared(Identifier(), ast.name)
        return [res.mtype]

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
        return [IntType()]

    def visitFloatLiteral(self, ast, c):
        return [FloatType()]

    def visitBooleanLiteral(self, ast, c):
        return [BoolType()]

    def visitStringLiteral(self, ast, c):
        return [StringType()]

