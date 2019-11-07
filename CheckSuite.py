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
        
        int foo(){ //Error
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_global_variable(self):
        """Simple program: int main() {} """
        input = """int a;
        string b,c, d;
        boolean m;
        float a; // Error
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_global_array(self):
        """Simple program: int main() {} """
        input = """int a[5];
        float a; // Error
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_global_array_function(self):
        """Simple program: int main() {} """
        input = """int foo(){}
        float[] foo(){} //Error
        void main(){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_mix_global_declaration(self):
        """Simple program: int main() {} """
        input = """int a,b,c;
        void foo(){}
        string a(){} // Error
        int foo(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_parameter(self):
        """More complex program"""
        input = """
            int a;
            int foo(float b, string b){ //Error
            }
            void main(){
            
            }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_parameter_inside_function(self):
        """More complex program"""
        input = """
            void foo1(){}
            void foo(int a, float b){
                string foo1;
                string b; //Error
            }
            void main(){
            
            }
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
            void main(){
            
            }
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
            void main(){
                
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    # Test undeclared
    def test_simple_undeclared_variable_in_function(self):
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
               foo(b);   
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
               foo(b); 
        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_use_variable_before_initialize_in_function(self):
        """More complex program"""
        input = """
            void main(){
                c;
                int c;
            }

        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_use_variable_before_initialize_in_block(self):
        """More complex program"""
        input = """
            void main(){
                int c;
                {
                    c;
                    d;
                    int d;
                }
            }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_pass_undeclared_variable_to_a_function_call(self):
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

    def test_undeclared_array(self):
        """More complex program"""
        input = """
            int a[5], b[5];
            void main(){
                a[2];
                b[4];
                c[5];
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_undeclared_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                
            }
            int a;
            float b;
            void main(){
                foo(a,b);
                foo1(a,b);
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_undeclared_function_inside_block(self):
        """More complex program"""
        input = """
            void foo(){}
            void foo1(int a, float b){
                {
                    foo();
                    foo1(a,b);
                    foo2();
                }
            }
            void main(){}
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_function_used_as_parameter(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
            }
            float b;
            void main(){
                foo(getInt(), b);
                foo(foo1(), b);
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_identifier_used_in_index_expression(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                
            }
            void main(){
                int b,a[5];
                a[b];
                a[d];
            }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_function_in_array_index_expression(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                
            }
            void main(){
                int b,a[5];
                float c;
                a[b];
                a[foo(b,c)];
                a[foo1(b,c)]; // Error
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_complex_program_undeclared_error(self):
        """More complex program"""
        input = """
             void main() { 
                    foo; 
                    test(); 
            }

            void test(){
                    foo(5);
            }

            int foo(int a){
                     foo(9);
                     return 3 ;
            }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test14(self):
        """More complex program"""
        input = """
            int f(){
                        
            }
            int main(){
                    int main;
                    main = f( );
                    putIntLn(main);
                    {
                        int i;
                        int main;                            
                        int f;
                        main = f = i = 100;
                        putIntLn(i);
                        putIntLn( main );
                        putIntLn(f);
                    }
                    putIntLn(main);
            }
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
                a + c; // Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_in_simple_subtract_statement(self):
        """Sub take only int or float for left and right expression"""
        input = """
            void main(){ 
                int a;
                float b;
                boolean c;
                a - b;
                b - a - a;
                a - c; //Error
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_simple_multiple_statement(self):
        """Multiply take only int or float for left and right expression"""
        input = """
            void main(){ 
                int a;
                float b;
                boolean c;
                a * b;
                b * a * a;
                a * c; //Error
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_in_simple_div_statement(self):
        """Divide take only int or float for left and right expression"""
        input = """
            void main(){
                int a;
                float b;
                boolean c;
                a / b;
                b / a / a;
                c / a; //Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_simple_module_statement(self):
        """Module only take int type for left and right hand-side expression"""
        input = """
            void main(){
                int a;
                float b;
                int c,d;
                a % c;
                a % c % d;
                b % a; // Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_in_simple_comparison_statement(self):
        """More complex program"""
        input = """
            void main(){
                int a;
                float b;
                int c,d;
                boolean e;
                a > c;
                (a > c) > d;
                b > a;
                e > c; // error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,BinaryOp(>,Id(a),Id(c)),Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_simple_equal_statement(self):
        """More complex program"""
        input = """
            void main(){ 
                int a, c;
                float b, d;
                a == c;
                b == d; // Error
                a == b;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_in_simple_not_equal_statement(self):
        """More complex program"""
        input = """
            void main(){
                int x,z;
                boolean y,z1;
                x != z;
                y != z1;
                x != y; //Error
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_simple_assign_statement(self):
        """More complex program"""
        input = """
            void main(){
                int a,a1;
                float b,b1;
                boolean c,c1;
                a = a1;
                b = b1;
                c = c1;
                b = a1;
                b = a + a1;
                a = b1; // Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b1))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_pass_less_parameter_to_a_function_call(self):
        """More complex program"""
        input = """
            void main(){
                getInt();
                getInt(4); //Error
            }
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
            void main(){
                int a;
                boolean b;
                foo(getInt(a),b); // Error
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_in_negative_expression(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                float b;
                boolean c;
                - a;
                - b;
                 -c; // Error
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_type_mismatch_in_simple_not_expression(self):
        """More complex program"""
        input = """
            void main(){ 
                boolean a, b;
                float c;
                !a;
                !b;
                -c;
                !c; // Error 
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_type_mismatch_in_simple_array_expression(self):
        """More complex program"""
        input = """
        int arr[5];
            void main( int b[]){    
                int a;           
                float c;
               a = arr[4];
               a = b[4];
               a = arr[b]; // Error since b has ArrayPointerType
               arr[c]; }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_complex_int_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int c;
            float d;
            void main(){
                int a, b;
                (a + ( b - c))/c + d;
                (b % a) + c * (c + d);
                (a/2 + b -10)/ 2 -10 * d % c; // Error since d is float so 10 * d is float type
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,BinaryOp(*,IntLiteral(10),Id(d)),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_complex_comparison_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                
            }
            void main(){
            int a, b;
            float c, d;
            boolean x;
            (a + 1) == (foo(a,c) -2); // Success
            foo(b, d) == 2 && x != true; // Success
            (foo(a,c) - a >= 0 || a - 1 <= 10) == 1; //Error since left hand side is boolean 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(||,BinaryOp(>=,BinaryOp(-,CallExpr(Id(foo),[Id(a),Id(c)]),Id(a)),IntLiteral(0)),BinaryOp(<=,BinaryOp(-,Id(a),IntLiteral(1)),IntLiteral(10))),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_complex_assign_expression_with_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                 
            }
            void main(){
                int arr[10];
                int a, b;
                float x ,y;
                a = b = 0; // success
                arr[a] = (x + y)/ 2 -10; // error since right hand side is Float type
                x = foo(a ,y);
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(arr),Id(a)),BinaryOp(-,BinaryOp(/,BinaryOp(+,Id(x),Id(y)),IntLiteral(2)),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_complex_array_index_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                a + b;
            }
            void main(){
                int a[10], d[5];
                int x;
                float y;
                a[foo(x, y) + 2 /10 % 5];
                a[x * y - foo(x,y)]; //Error since x * y - foo(x,y) is float type not int
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,Id(x),Id(y)),CallExpr(Id(foo),[Id(x),Id(y)])))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_mix_all_expression(self):
        """More complex program"""
        input = """
            int[] foo(int a){
                
            }
            void main(){
                int i[10], b[10], a [10];
                int c,d, x;
                (1 + 1*2 -3/4*5%6) == 2;        //Success
                !true || !false != true;         //Success
                i[1 *3 +4/2 - 5%1];              //Success
                foo(2)[3+x] = a[b[2]] +3;        //Success
                a[i[9] - b[3] + c - d] != b[12]; //Success
                foo(3)[true && false] == foo(2)[foo(3)[2] - true]; //Error
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[IntLiteral(3)]),BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    # Statement checking
    def test_type_mismatch_in_if_statement(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                int c;
                if(a == 0)
                    b + 1;
                
                if(b)
                    b + 1;
            }
            void main(){}
        """
        expect = "Type Mismatch In Statement: If(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_inside_if_else_statement(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                float b;
                if(a == 0)
                    b + 1;
                else
                    b + 2;
                
                
                if(b)       // Error
                    b + 1;
                else
                    b +2;    
            }
        """
        expect = "Type Mismatch In Statement: If(Id(b),BinaryOp(+,Id(b),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_mismatch_type_in_simple_do_while_statement(self):
        """More complex program"""
        input = """  
            void main(){  
                int a;
                float b; 
                do
                    a + 1;
                while( a < 10);
                
                do 
                    b+1;
                while( b);      // Error
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(+,Id(b),IntLiteral(1))],Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_mismatch_in_simple_for_statement_expression_1(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
               int c;
               for(c; c <a; c = c+1){ // Success
                    b = b+1;
               }
                for(b; c <a; c = c+1){ // Error
                    b = b+1;
               }
            }
            int a;
            float b;
            void main(){
                foo(a,b);
            }
        """
        expect = "Type Mismatch In Statement: For(Id(b);BinaryOp(<,Id(c),Id(a));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_mismatch_in_simple_for_statement_expression_2_(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                c;
            }
            void main(){
                 foo(a,b);
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test42(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                int c;
                c = 0;
                for(c =0; c< a; c = c+1){ // Break in if inside for is ok
                    if(a % c == 0)
                        break;
                    
                }
                if(a == c) // this will cause error
                    break;
            }
            void main(){
                 foo(a,b);
            }
        """
        expect = "Break Not In Loop"
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
                foo(a,b);
            }
            void main(){ 
               
            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test47(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test48(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test49(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test50(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test51(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test52(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test53(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test54(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test55(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test56(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test57(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test58(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test59(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test60(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test61(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test62(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test63(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test64(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test65(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test66(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test67(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test68(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test69(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test70(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test71(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test72(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                foo(a,b);
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 482))

