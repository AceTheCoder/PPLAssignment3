# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_declare.
    def visitFunction_declare(self, ctx:MCParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_decl.
    def visitParameter_decl(self, ctx:MCParser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_list.
    def visitParameter_list(self, ctx:MCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter.
    def visitParameter(self, ctx:MCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable_declare.
    def visitVariable_declare(self, ctx:MCParser.Variable_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variables_list.
    def visitVariables_list(self, ctx:MCParser.Variables_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_list.
    def visitExpression_list(self, ctx:MCParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_input_parameter.
    def visitArray_input_parameter(self, ctx:MCParser.Array_input_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_output_pointer.
    def visitArray_output_pointer(self, ctx:MCParser.Array_output_pointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_type.
    def visitFunction_type(self, ctx:MCParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#no_else_if_statement.
    def visitNo_else_if_statement(self, ctx:MCParser.No_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#have_else_if_statement.
    def visitHave_else_if_statement(self, ctx:MCParser.Have_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhile_statement.
    def visitDowhile_statement(self, ctx:MCParser.Dowhile_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmts.
    def visitBlock_stmts(self, ctx:MCParser.Block_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_statement.
    def visitExpression_statement(self, ctx:MCParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_element.
    def visitArray_element(self, ctx:MCParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#nonassoc_bool_expression.
    def visitNonassoc_bool_expression(self, ctx:MCParser.Nonassoc_bool_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assoc_int_expression.
    def visitAssoc_int_expression(self, ctx:MCParser.Assoc_int_expressionContext):
        return self.visitChildren(ctx)



del MCParser