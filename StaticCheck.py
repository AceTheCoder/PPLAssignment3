
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
    def __init__(self, name, mtype, value=None, kind=Identifier(), is_global=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.is_global = is_global

    def getKind(self):
        return self.kind

    def getName(self):
        return self.name

    def toGlobal(self):
        self.is_global = True
        return self

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

    # def toString(self):
    #     return self.name + " " + str(self.mtype) + " " + str(self.kind)


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
        if type(paraType) == type(patternType):
            return True
        return False


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
        # if self.lookup(ast.name.name, c, lambda x: x.name) is None:
        try:
            para = [Symbol.getSymbolFromDecl(x) for x in ast.param]
            para = CheckError.checkRedeclared([], para)
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        globl = [[Symbol.getSymbolFromFunction(ast)] + c[0]]
        env = [para] + globl
    # local_variable = functools.reduce(lambda env, decl: [Checker.checkRedeclared(env[0], self.visit(decl, env))] if
    #             type(decl) is VarDecl else [env[0] + self.visit(decl, (env, True))], ast.body.member, [para] + globl)
        body_statement = []
        for decl in ast.body.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env)), env[1]]
            else:
                body_statement += self.visit(decl, (env, ast.returnType, False, ast.name.name, c[1]))
        return [Symbol.getSymbolFromFunction(ast)]

    def visitVarDecl(self, ast, c):
        return [Symbol.getSymbolFromVarDecl(ast)]

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

    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen, self.visit(ast.eleType, c))

    def visitArrayPointerType(self, ast, c):
        return ArrayPointerType(self.visit(ast.eleType, c))

    def visitIntLiteral(self, ast, c):
        return [IntType()]

    def visitBooleanLiteral(self, ast, c):
        return [BoolType()]

    def visitStringLiteral(self, ast, c):
        return [StringType()]

    def visitBlock(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        env = [[]] + scope
        for decl in ast.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env))] + env[::1]
            else:
                self.visit(decl, (env, function_type, in_loop, function_name, invoked_function))
    # functools.reduce(lambda env, decl: [env[0] + self.visit(decl, (env, True))] if
    # type(decl) is not VarDecl else [Checker.checkRedeclared(env[0], self.visit(decl, env))], ast.member, [[]] + c[0])
        return []

    # unfinished
    def visitIf(self, ast, c):
        condition = self.visit(ast.expr, c)
        if type(condition[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmts1 = self.visit(ast.thenStmt, c)
        if ast.elseStmt is not None:
            stmts2 = self.visit(ast.elseStmt, c)
        return [ast]

    def visitDowhile(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        condition = self.visit(ast.exp, c)
        if type(condition[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmt_list = [self.visit(x, (scope, function_type, True, function_name, invoked_function)) for x in ast.sl]
        return [ast]

    def visitFor(self, ast, c):
        scope, function_type, in_loop, function_name, invoked_function = c
        condition1 = self.visit(ast.expr1, c)
        condition2 = self.visit(ast.expr2, c)
        condition3 = self.visit(ast.expr3, c)
        if type(condition1[0]) is not IntType or type(condition3[0]) is not IntType or type(condition2[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        loopStmt = self.visit(ast.loop, (scope, function_type, True, function_name, invoked_function))
        return [ast]

    def visitBreak(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise BreakNotInLoop()
        else:
            return [ast]

    def visitContinue(self, ast, c):
        scope, return_type, in_loop, function_name, invoked_function = c
        if not in_loop:
            raise ContinueNotInLoop()
        else:
            return [ast]

    def visitReturn(self, ast, c):
        return []

    # Expression
    def visitBinaryOp(self, ast, c):
        op = ast.op
        lefths = self.visit(ast.left, c)
        left = type(lefths[0])
        righths = self.visit(ast.right, c)
        right = type(righths[0])
        if op == '%':
            if left is not IntType or right is not IntType:
                raise TypeMismatchInExpression(ast)
            return [IntType()]
        elif op in ['+', '-', '*', '/']:
            if left not in [IntType, FloatType] or right not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return [lefths[0]] if left is right else [FloatType()]
        elif op in ['>', '>=', '<', '<=']:
            if left not in [IntType, FloatType] or right not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op in ['==', '!=']:
            if left is not right or left not in [IntType, BoolType]:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op in ['&&', '||']:
            if left is not BoolType or right is not BoolType:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op == '=':
            if left in [VoidType, ArrayPointerType, ArrayType]:
                raise TypeMismatchInExpression(ast)
            elif left is not FloatType:
                if right is not left: raise TypeMismatchInExpression(ast)
            else:
                if right not in [FloatType, IntType]:
                    raise TypeMismatchInExpression(ast)
            return [lefths[0]]

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
        env, return_type, in_loop, function_name, invoked_function = c
        scope = [x for y in env for x in y]
        at = [self.visit(x, (env, None, in_loop, function_name, invoked_function))[0] for x in ast.param]
        res = self.lookup(ast.method.name, scope, lambda x: x.name) #if isinstance(x, Symbol) else None)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
        elif not CheckError.checkMatchingParameter(at, res.mtype.partype):
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
        else:
            return [res.mtype]
