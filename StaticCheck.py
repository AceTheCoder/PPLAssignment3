
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
        decl_list = [Symbol.getSymbolFromDecl(x) for x in ast.decl]
        decl_list = CheckError.checkRedeclared(StaticChecker.global_envi, decl_list)
        entryPoint1 = Symbol("main", MType([], VoidType()), kind=Function())
        res = self.lookup(entryPoint1.name, decl_list, lambda x: x.name)
        if res is None:
            raise NoEntryPoint()
        else:
            if type(res.kind) is not type(entryPoint1.kind):
                raise NoEntryPoint()
        visit = [self.visit(decl, [decl_list]) for decl in ast.decl]
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
        for decl in ast.body.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env)), env[1]]
            else:
                self.visit(decl, (env, True))
        return [Symbol.getSymbolFromFunction(ast)]

    def visitVarDecl(self, ast, c):
        return [Symbol.getSymbolFromVarDecl(ast)]

    def visitIntType(self, ast, c):
        return [IntType()]

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitFloatType(self, ast, c):
        return [FloatType()]

    def visitBooleanType(self, ast, c):
        return [BoolType()]

    def visitStringType(self, ast, c):
        return StringType()

    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen, self.visit(ast.eleType, c))

    def visitArrayPointerType(self, ast, c):
        return ArrayPointerType(self.visit(ast.eleType, c))

    def visitIntLiteral(self, ast, c):
        return [IntType()]

    def visitBlock(self, ast, c):
        env = [[]] + c[0]
        for decl in ast.member:
            if type(decl) is VarDecl:
                env = [CheckError.checkRedeclared(env[0], self.visit(decl, env))]
            else:
                self.visit(decl, (env, True))
        # functools.reduce(lambda env, decl: [env[0] + self.visit(decl, (env, True))] if
        # type(decl) is not VarDecl else [Checker.checkRedeclared(env[0], self.visit(decl, env))], ast.member, [[]] + c[0])
        return []

    # unfinished
    def visitIf(self, ast, c):
        condition = self.visit(ast.expr, c)
        if type(condition) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stmts1 = [self.visit(x, c) for x in ast.thenStmt]
        stmts2 = [self.visit(x, c) for x in ast.elseStmt]

    def visitDoWhile(self, ast, c):
        return []

    def visitFor(self, ast, c):
        return []

    def visitBreak(self, ast, c):
        return []

    def visitContinue(self, ast, c):
        return []

    def visitReturn(self, ast, c):
        return []

    # Expression
    def visitBinaryOp(self, ast, c):
        op = ast.op
        lefths = self.visit(ast.left, c)
        left = type(lefths[0])
        righths = self.visit(ast.right, c)
        right = type(righths[0])
        if left is StringType() or right is StringType():
            raise TypeMismatchInExpression(ast)
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
            if left is not right or left not in [IntType, BoolType] or right not in [IntType, BoolType]:
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op in ['&&', '||']:
            if left is not BoolType() or right is not BoolType():
                raise TypeMismatchInExpression(ast)
            return [BoolType()]
        elif op == '=':
            if left is not FloatType:
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
        scope = [x for y in c[0] for x in y]
        at = [self.visit(x, (c[0], False))[0] for x in ast.param]
        res = self.lookup(ast.method.name, scope, lambda x: x.name if isinstance(x, Symbol) else None)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
        elif not CheckError.checkMatchingParameter(at, res.mtype.partype):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return [res.mtype.rettype]

    def visitId(self, ast, c):
        scope = [x for y in c[0] for x in y]
        res = self.lookup(ast.name, scope, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return [res.mtype]
