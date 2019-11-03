
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


class Symbol:
    def __init__(self, name, mtype, value=None, kind=Identifier()):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind

    def getKind(self):
        return self.kind

    def getName(self):
        return self.name

    # def __eq__(self, other):
    #     return self.name == other.name and self.mtype == other.mtype and self.kind == other.kind

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

# class Checker:
#     utils = Utils()
#
#     @staticmethod
#     def checkRedeclared(Scope, Symbollist):
#         newScope = Scope.copy()
#         for x in Symbollist:
#             f = Checker.utils.lookup(x.name, newScope, Symbol.getName)
#             if f is not None:
#                 raise Redeclared(x.kind, x.name)
#             newScope.append(x)

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
        # decl_list = [Symbol.getSymbolFromDecl(x) for x in ast.decl]
        # Checker.checkRedeclared(StaticChecker.global_envi, decl_list)
        # entryPoint = Symbol('main', MType([], IntType()), kind=Function())
        # entryPoint1 = Symbol('main', MType([], VoidType()), kind=Function())
        # if self.lookup(entryPoint, decl_list, lambda x: x) is None and self.lookup(entryPoint, decl_list, lambda x:x) is None:
        #     raise NoEntryPoint()
        # visit = [self.visit(decl, decl_list) for decl in ast.decl]
        visit_list = functools.reduce(lambda env, decl: env + [self.visit(decl, env)], ast.decl, c)
        res = self.lookup('main', visit_list, lambda x: x.name)
        if res is not None:
            if res.mtype != MType([], IntType()) or res.mtype != ([], VoidType()):
                raise NoEntryPoint()
        else:
            raise NoEntryPoint()


    def visitFuncDecl(self, ast, c):
        if self.lookup(ast.name.name, c, lambda x: x.name) is None:
            try:
                para = functools.reduce(lambda env, decl: env + [self.visit(decl, env)], ast.param, [])
                # Checker.checkRedeclared([], para)
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
            local_variable = functools.reduce(lambda env, decl: env + [self.visit(decl, env)],
                                            list(filter(lambda x: type(x) is VarDecl, ast.body.member)), para)
            # local_variable = list(filter(lambda x: type(x) is VarDecl, ast.body.member))
            # Checker.checkRedeclared(para, local_variable)
            variable = c + local_variable
            body_statement = list(map(lambda decl: self.visit(decl, (variable, True)),
                                            list(filter(lambda x: type(x) is not VarDecl, ast.body.member))))
            return Symbol.getSymbolFromFunction(ast)
        else:
            raise Redeclared(Function(), ast.name.name)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c, lambda x: x.name) is None:
            return Symbol.getSymbolFromVarDecl(ast)
        else:
            raise Redeclared(Variable(), ast.variable)

    def visitCallExpr(self, ast, c):
        at = [self.visit(x, (c[0], False)) for x in ast.param]
        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return Symbol(res.name, res.mtype)

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

    def visitId(self, ast, c):
        if self.lookup(ast.name, c[0], lambda x: x.name) is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return Symbol(ast.name, [] , kind = Identifier())
