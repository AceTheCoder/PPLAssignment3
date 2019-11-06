import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_main_function(self):
        """Simple program: int main() {} """
        input = """int foo() {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_global_main_variable_declare(self):
        """More complex program"""
        input = """int main;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_function_name(self):
        """More complex program"""
        input = """int foo() {
        }
        void main(){}
        
        int foo(){
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_global_variable(self):
        """Simple program: int main() {} """
        input = """int a;
        string b,c, d;
        boolean m;
        float a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_global_array(self):
        """Simple program: int main() {} """
        input = """int a[5];
        float a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_global_array_function(self):
        """Simple program: int main() {} """
        input = """int foo(){}
        float[] foo(){}
        void main(){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_mix_global_declaration(self):
        """Simple program: int main() {} """
        input = """int a,b,c;
        void foo(){}
        string a(){}
        int foo(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_parameter(self):
        """More complex program"""
        input = """
            int a;
            int foo(float b, string b){
            }
            void main(){}
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_parameter_inside_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                string b;
            }
            void main(){}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclare_parameter_inside_block(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                {
                    int a;
                    int b,c,d;
                    float a;    
                }
            }
            void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclare_array_pointer_parameter(self):
        """More complex program"""
        input = """
            void foo(int a, float b[], float a[]){
               b;
            }
            int c;
            void main(){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    # Test undeclared
    def test_simple_undeclared_in_function(self):
        """More complex program"""
        input = """
        int a,b,d;
        int foo(int a){
            int c;
            a;
            b + d;
            m;
        }
        void main() {
                
        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undeclared_in_block_statement(self):
        """More complex program"""
        input = """
        int b,d;
        int foo(int a){
            int c;
            {
                c;
                d = a + b;
                a = m;
            }
        }
        int main() {
                
        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_use_variable_before_initialize_in_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
                int c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_use_variable_before_initialize_in_block(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                int c;
                {
                    c;
                    d;
                    int d;
                }
            }
            void main(){}
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_pass_undeclared_variable_to_a_functioncall(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                putIntLn(4);
                putIntLn(a);
                putIntLn(c);
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test7(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test8(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test9(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test10(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test11(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test12(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test13(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test14(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test15(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 424))

    # Check type mismatch in expression
    def test_type_mismatch_in_simple_add_statement(self):
        """Add take only int or float for left and right expression"""
        input = """
            void main(){
                int a;
                float b;
                boolean c;
                (a + b) + a;
                a + c;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_in_simple_subtract_statement(self):
        """Sub take only int or float for left and right expression"""
        input = """
            void foo(int a, float b){
                boolean c;
                a - b;
                b - a - a;
                a - c; 
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_simple_multiple_statement(self):
        """Multiply take only int or float for left and right expression"""
        input = """
            void foo(int a, float b){
                boolean c;
                a * b;
                b * a * a;
                a * c; 
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_in_simple_div_statement(self):
        """Divide take only int or float for left and right expression"""
        input = """
            void foo(int a, float b){
                boolean c;
                a / b;
                b / a / a;
                c / a; 
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_simple_module_statement(self):
        """Module only take int type for left and right hand-side expression"""
        input = """
            void foo(int a, float b){
                int c,d;
                a % c;
                a % c % d;
                b % a;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_in_simple_comparison_statement(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                int c,d;
                boolean e;
                a > c;
                (a > c) > d;
                b > a;
                e > c;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,BinaryOp(>,Id(a),Id(c)),Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_simple_equal_statement(self):
        """More complex program"""
        input = """
            void foo(int a, boolean b){
                int c;
                boolean d;
                a == c;
                b == d;
                a == b;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_in_simple_not_equal_statement(self):
        """More complex program"""
        input = """
            void foo(int x, boolean y){
                int z;
                boolean z1;
                x != z;
                y != z1;
                x != y;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_simple_assign_statement(self):
        """More complex program"""
        input = """
            void foo(int a, float b, boolean c){
                int a1;
                float b1;
                boolean c1;
                a = a1;
                b = b1;
                c = c1;
                b = a1;
                b = a + a1;
                a = b1;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b1))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_pass_less_parameter_to_a_function_call(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                getInt();
                getInt(4);
            }
            void main(){}
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_pass_more_parameter_to_a_function_call(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                
            }
            int a, c;
            void main(){
               float b;
               foo(a,b);
               foo(a, b, 4);
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(foo),[Id(a),Id(b),IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_pass_wrong_type_to_a_function_call(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                
            }
            int a;
            void main(){
               boolean b;
               float c;
               foo(a,c);
               foo(a, b);
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_pass_wrong_type_to_a_function_call_in_an_expression(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                
            }
            void main(){
                int a;
                boolean b;
                foo(getInt(a),b);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_in_negative_expression(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                boolean c;
                - a;
                - b;
                 -c;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_type_mismatch_in_simple_not_expression(self):
        """More complex program"""
        input = """
            void foo(boolean a, boolean b){
                int c;
                !a;
                !b;
                -c;
                !c;
            }
            void main(){}
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test31(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test32(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test33(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test34(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test35(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test36(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test37(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test38(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test39(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test40(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test41(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test42(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test43(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test44(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test45(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test46(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 455))

