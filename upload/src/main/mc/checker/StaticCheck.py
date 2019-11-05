
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
    def __init__(self, name, mtype, value=None, kind=Identifier(), Is_global=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.Is_global = Is_global

    def getKind(self):
        return self.kind

    def getName(self):
        return self.name

    def toGlobal(self):
        self.Is_global = True
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

class Checker:
    utils = Utils()

    @staticmethod
    def checkRedeclared(scope, symbol_list):
        new_scope = scope.copy()
        for x in symbol_list:
            f = Checker.utils.lookup(x.name, new_scope, Symbol.getName)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            new_scope.append(x)
        return new_scope


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
        decl_list = Checker.checkRedeclared(StaticChecker.global_envi, decl_list)
        entryPoint1 = Symbol("main", MType([], VoidType()), kind=Function())
        res = self.lookup(entryPoint1.name, decl_list, lambda x: x.name)
        if res is None:
            raise NoEntryPoint()
        else:
            if str(res.mtype) != str(entryPoint1.mtype):
                raise NoEntryPoint()
        visit = [self.visit(decl, [decl_list]) for decl in ast.decl]
        return visit

    def visitFuncDecl(self, ast, c):
        # if self.lookup(ast.name.name, c, lambda x: x.name) is None:
        try:
            para = [Symbol.getSymbolFromDecl(x) for x in ast.param]
            para = Checker.checkRedeclared([], para)
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        globl = [[Symbol.getSymbolFromFunction(ast)] + c[0]]
        local_variable = functools.reduce(lambda env, decl: [Checker.checkRedeclared(env[0], self.visit(decl, env))], ast.body.member, [para] + globl)
        return [Symbol.getSymbolFromFunction(ast)]

    def visitVarDecl(self, ast, c):
        return [Symbol.getSymbolFromVarDecl(ast)]

    # def visitCallExpr(self, ast, c):
    #     at = [self.visit(x, (c[0], False)) for x in ast.param]
    #     res = self.lookup(ast.method.name, c[0], lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(), ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return Symbol(res.name, res.mtype)

    def visitIntType(self, ast, c):
        return IntType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBooleanType(self, ast, c):
        return BooleanType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen, self.visit(ast.eleType, c))

    def visitArrayPointerType(self, ast, c):
        return ArrayPointerType(self.visit(ast.eleType, c))

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBlock(self, ast, c):
        functools.reduce(lambda env, decl: [env[0] + self.visit(decl, env)], ast.member, [[]] + c)
        return []

    def visitIf(self, ast, c):

    def visitId(self, ast, c):
        scope = [x for y in c for x in y]
        res = self.lookup(ast.name, scope, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return []
