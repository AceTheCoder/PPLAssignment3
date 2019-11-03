//1752063
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  :  declaration+ EOF;

//===========================================================================//
//mctype: INTTYPE | VOIDTYPE;

declaration: function_declare | variable_declare;

function_declare: function_type ID parameter_decl block_statement;

parameter_decl : LB parameter_list RB;

parameter_list: (parameter) (COMMA parameter)* | ;

parameter: primitive_type ID | array_input_parameter;



variable_declare: primitive_type variables_list SEMI;

variables_list: variable (COMMA variable)*;

variable: ID LSB INTLIT RSB | ID;

//array: ID LSB INTLIT RSB;



expression_list: expression (COMMA expression)*;

array_input_parameter: primitive_type ID LSB RSB;

array_output_pointer: primitive_type LSB RSB;

array_pointer_type: array_input_parameter | array_output_pointer;

primitive_type: INTTYPE | BOOLEANTYPE | FLOATTYPE | STRINGTYPE;

function_type: INTTYPE | BOOLEANTYPE | FLOATTYPE | STRINGTYPE | VOIDTYPE | array_output_pointer;

//===========================================================================//
//Statement
statement: if_statement
| dowhile_statement
| for_statement
| break_statement
| continue_statement
| return_statement
| block_statement
| expression_statement;


if_statement: no_else_if_statement | have_else_if_statement;
no_else_if_statement:
                IF LB expression RB
                    statement
                ;


have_else_if_statement:
                IF LB expression RB
                    statement
                ELSE
                    statement;


dowhile_statement:
                DO
                    statement+
                WHILE expression SEMI;


for_statement:
                FOR LB expression SEMI expression SEMI expression RB
                    statement
                ;


break_statement:
                BREAK SEMI;


continue_statement:
                CONTINUE SEMI;


return_statement: RETURN expression? SEMI;


block_statement:
                LP
                    block_stmts*
                RP;

block_stmts: (variable_declare | statement);


expression_statement:
                expression SEMI;



operands: literal | funcall | ID | array_element;

array_element: (funcall | ID ) LSB expression RSB;

literal: INTLIT | BOOLLIT | FLOATLIT | STRINGLIT;

funcall: ID LB expression_list? RB;

//===========================================================================//
//Expression
 expression:
 LB expression RB
| expression LSB expression RSB
| <assoc=right> (MINUSOP | NOT) expression
| <assoc=left> expression (MULOP | DIVOP | MODOP) expression
| <assoc=left> expression (ADDOP | MINUSOP) expression
| assoc_int_expression (LT | ST | LE | SE) assoc_int_expression
| nonassoc_bool_expression (EQUAL | NOTEQUAL) nonassoc_bool_expression
| <assoc=left> expression AND expression
| <assoc=left> expression OR expression
| <assoc=right> expression ASSIGN expression
| operands;



nonassoc_bool_expression: LB expression RB
| nonassoc_bool_expression LSB nonassoc_bool_expression RSB
| <assoc=right> (MINUSOP | NOT) nonassoc_bool_expression
| <assoc=left> nonassoc_bool_expression (MULOP | DIVOP | MODOP) nonassoc_bool_expression
| <assoc=left> nonassoc_bool_expression (ADDOP | MINUSOP) nonassoc_bool_expression
//| assoc_int_expression
| assoc_int_expression (LT | ST | LE | SE) assoc_int_expression
//| assoc_int_expression (EQUAL | NOTEQUAL) assoc_int_expression
//| <assoc=left> nonassoc_bool_expression AND nonassoc_bool_expression
//| <assoc=left> nonassoc_bool_expression OR nonassoc_bool_expression
| operands;



assoc_int_expression: LB expression RB
| assoc_int_expression LSB assoc_int_expression RSB
| <assoc=right> (MINUSOP | NOT) assoc_int_expression
| <assoc=left> assoc_int_expression (MULOP | DIVOP | MODOP) assoc_int_expression
| <assoc=left> assoc_int_expression (ADDOP | MINUSOP) assoc_int_expression
| operands;


//===========================================================================//

//Keyword
BREAK: 'break' ;

CONTINUE: 'continue' ;

FOR: 'for' ;

DO: 'do' ;

WHILE: 'while' ;

IF: 'if' ;

ELSE: 'else' ;

RETURN: 'return' ;

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLEANTYPE: 'boolean' ;

FLOATTYPE: 'float' ;

STRINGTYPE: 'string' ;

fragment TRUE: 'true' ;

fragment FALSE: 'false' ;

//===========================================================================//

//Operator
EQUAL: '==';

NOTEQUAL: '!=';

ASSIGN: '=';

ADDOP: '+';

MINUSOP: '-';

MULOP: '*';

DIVOP: '/';

MODOP: '%';

AND: '&&';

OR: '||';

NOT: '!';

LT: '>'; //Larger than

ST: '<';//Smaller than

LE: '>='; // Larger or equal

SE: '<=';// Smaller or equal

//===========================================================================//

//Seperators
LSB: '[';

RSB: ']';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',' ;

COLON: ':';

//===========================================================================//

//Comment
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

//===========================================================================//
//Literal

BOOLLIT: TRUE | FALSE;

INTLIT: [0-9]+;

FLOATLIT: WP FP? | INTLIT EXPONENT | '.' FP;
fragment WP: INTLIT '.';
fragment FP: INTLIT | INTLIT? EXPONENT?;
fragment EXPONENT: [Ee] MINUSOP? INTLIT;

STRINGLIT: DOUBLEQUOTE (STRCHAR | ESCAPE_SEQ)* DOUBLEQUOTE {self.text = self.text.replace('"',"")};
fragment DOUBLEQUOTE: '"';
fragment STRCHAR: ~('\\'|'"'| '\n' | '\r' | '\b' | '\f' |'\t');
fragment ESCAPE_SEQ: '\\' [brntf"\\];
fragment NOT_ESCAPE_SEQ:  '\\' ~[btfrn"\\];

ID: [a-zA-Z_][0-9a-zA-Z_]*;

MAIN: 'main' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . | FLOATLIT '.';
UNCLOSE_STRING: DOUBLEQUOTE (STRCHAR | ESCAPE_SEQ)* (EOF | [\r\n]) {self.text = self.text.lstrip('"').rstrip("\n\r")};
ILLEGAL_ESCAPE: DOUBLEQUOTE (STRCHAR | ESCAPE_SEQ)* NOT_ESCAPE_SEQ {self.text = self.text.lstrip('"')};