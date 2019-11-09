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
        input = """void foo() {
        }
        void main(){
            foo();
        }
        
        void foo(){ //Error
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_global_variable(self):
        """Simple program: int main() {} """
        input = """int a;
        string b,c, d;
        boolean m;
        float a;        // Error
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_global_array(self):
        """Simple program: int main() {} """
        input = """int a[5];
        float a;        // Error
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_global_array_function(self):
        """Simple program: int main() {} """
        input = """int[] foo(){}
        float[] foo(){}         //Error
        void main(){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_mix_global_declaration(self):
        """Simple program: int main() {} """
        input = """int a,b,c;
        void foo(){}
        string a(){}        // Error
        int foo(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_parameter(self):
        """More complex program"""
        input = """
            int a;
            int foo(float b, string b){      //Error
            }
            void main(){
            
            }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_parameter_inside_function(self):
        """More complex program"""
        input = """
            void foo1(){ return ;}
            void foo(int a, float b){
                string foo1;
                string b;           //Error
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
                    float a;        // Error
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
        void foo(int a){
            int c;
            a;
            b + d;
            m;  //Error
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
                a = m;  //Error
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
                c;  //Error
                int c; 
            }

        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_use_variable_before_initialize_in_block(self):
        """More complex program"""
        input = """
            void main(){
                {
                    int c;
                }
                {
                    c;  // Error
                }
                
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_pass_undeclared_variable_to_a_function_call(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                putIntLn(4);
                putIntLn(a);
                putIntLn(c);  //Error
                return;
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
                c[5];   //Error
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_simple_undeclared_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                return ;
            }
            int a;
            float b;
            void main(){
                foo(a,b);
                foo1(a,b); //Error
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_undeclared_function_inside_block(self):
        """More complex program"""
        input = """
            void foo(){ 
                return;
                }
            void foo1(int a, float b){
                {
                    foo();
                    foo1(a,b);
                    foo2();     //Error
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
                return;
            }
            float b;
            void main(){
                foo(getInt(), b);
                foo(foo1(), b);     //Error
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_identifier_used_in_index_expression(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                return a;
            }
            void main(){
                int b,a[5];
                a[b];
                a[d];           //Error
            }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_function_in_array_index_expression(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                return a;
            }
            void main(){
                int b,a[5];
                float c;
                a[b];
                a[foo(b,c)];
                a[foo1(b,c)];   // Error
            }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared_identifier_in_statement(self):
        """More complex program"""
        input = """
            int main()
            {
            int array0[7];
            int array1[7];
        
            int sum[7]; 
            for(i = 0; i < 7; i = i +1)    // Error
                    sum[i] = array0[i] + array1[i];
            }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_complex_program_with_undeclared(self):
        """More complex program"""
        input = """
            int f(){
                   return 200;     
            }
            int main(){
                    int main;
                    main = f( );
                    putIntLn(main);
                    {
                        int i;
                        {
                        int main;                            
                        main = f = i = 100;  // Error
                        putIntLn(i);
                        putIntLn( main );
                        }
                    }
                    putIntLn(main);
                    return 0;
            }
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_complex_program_with_undeclared_extra_test(self):
        """More complex program"""
        input = """
            void main() { 
                    foo;  //Error
                    test(); 
            }

            void test(){
                    foo(5);
            }

            int foo(int a){
                     foo(9);
                     return 3;
            }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))

    # Check type mismatch in expression
    def test_type_mismatch_in_simple_add_statement(self):
        """Add take only int or float for left and right expression"""
        input = """
            void main(){
                int a;
                float b;
                boolean c;
                -10.5454 + 5;
                a + 3;
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
                a - 3;
                1 - 10.6969;
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
                a * 365;
                2 * a;
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
                a / 10;
                10 / a;
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
                a % 2;
                2 % a;
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
                (a < c) >= d; // error
                b <= a;
                e > c; 
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,BinaryOp(<,Id(a),Id(c)),Id(d))"
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

    def test_type_mismatch_in_simple_and_statement(self):
        """More complex program"""
        input = """
              void main(){ 
                  int a, c;
                  boolean b, d;
                  b && d ;
                  a == c && b; 
                  a && b;       // Error
              }
          """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_type_mismatch_in_simple_or_statement(self):
        """More complex program"""
        input = """
              void main(){ 
                 int a, c;
                  boolean b, d;
                  b || true ;
                  false || b; 
                  b == true || d;
                  a || false;   // Error
              }
          """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_type_mismatch_in_simple_assign_statement(self):
        """More complex program"""
        input = """
            void main(){
                int a,a1;
                float b,b1;
                boolean c,c1;
                string d;
                a = 10;
                b = 1.523;
                c = true;
                d = "Hello world";
                b = a1;
                b = a + a1;
                a = b1; // Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b1))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_pass_less_parameter_to_a_function_call(self):
        """More complex program"""
        input = """
            int foo(int a){
                return (a*2);
            }
            void main(){
                foo(4);
                foo();  //Error
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 436))

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
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_pass_wrong_type_to_a_function_call(self):
        """More complex program"""
        input = """
            void foo(int a, float b[]){
                return;
            }
            int a;
            void main(){
               int b[5];
               float c[5];
               foo(a, c);
               foo(a, b);
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_pass_wrong_type_to_a_function_call_in_an_expression(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                return;
            }
            int goo(int a){
                return a*2;
            }
            void main(){
                int a;
                boolean b;
                float c;
                foo(goo(4), 1.5);
                goo( foo(1, 3));    // Error

            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(goo),[CallExpr(Id(foo),[IntLiteral(1),IntLiteral(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_type_mismatch_in_negative_expression(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                float b;
                boolean c;
                - a;
                - b;
                - c; // Error
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 440))

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
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_type_mismatch_in_simple_index_expression(self):
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
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_array_index_mismatch_type_extra_test(self):
        """More complex program"""
        input = """
            void main(){
                int a, b[5];
                b[2] = a;
                b[4] = 0;
                a[0] = 1;
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_array_passing_in_function_call_expression(self):
        """More complex program"""
        input = """
            int[] foo(int a, int b[]){
                int c[5];
                if( a == 0){
                    c[0] = foo(a-1,b)[0];
                }
                return c;
            }
            void main(){
                float c[4];
                int a[3];
                foo(1, a);
                foo(2, foo(3, a));
                foo(9, c); //Error
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(foo),[IntLiteral(9),Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_build_in_Int_function(self):
        """More complex program"""
        input = """
               void main(){
                   int a;
                   a = getInt();
                   putIntLn(4);
                   putIntLn(a);
                   putInt(4);
                   putInt(a);
                   putInt("Hello");    //Error
               }
           """
        expect = "Type Mismatch In Statement: CallExpr(Id(putInt),[StringLiteral(Hello)])"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_build_in_Float_function(self):
        """More complex program"""
        input = """
                void main(){
                   float a;
                   a = getFloat();
                   a = getInt();
                   putFloatLn(4);
                   putFloatLn(a);
                   putFloat(4);
                   putFloat(a);
                   putFloat(true);
               }
           """
        expect = "Type Mismatch In Statement: CallExpr(Id(putFloat),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_build_in_Bool_function(self):
        """More complex program"""
        input = """
              void main(){
                   boolean x;
                   x = true;
                   putBoolLn(true);
                   putBoolLn(x);
                   putBool(false);
                   putBool(x);
                   putBool(1); //Error
               }
           """
        expect = "Type Mismatch In Statement: CallExpr(Id(putBool),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_build_in_String_function(self):
        """More complex program"""
        input = """
              void main(){
                   string x;
                   x = "Goodbye";
                   putStringLn("Assignment 3");
                   putStringLn("x");
                   putString("Hello");
                   putString(x);
                   putLn();
                   putString(169); //Error
               }
           """
        expect = "Type Mismatch In Statement: CallExpr(Id(putString),[IntLiteral(169)])"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_when_call_function_main(self):
        """More complex program"""
        input = """
             void foo(int a, float b){
                foo(a,b);
            }
            void main(){
                int a;
                float b;
                foo(a,b);
                main(a);
            }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(main),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_complex_int_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int c;
            float d;
            void main(){
                int a, b;
                (a + ( b - c))/c + d;
                (b % a) + c * (c + d);
                (a/2 + b -10)/ 2 -10 * d % c; // Error
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,BinaryOp(*,IntLiteral(10),Id(d)),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_complex_comparison_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                return a;
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
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_complex_assign_expression_with_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                 return a;
            }
            void main(){
                int arr[10];
                int a, b;
                float x ,y;
                a = b = 0; 
                arr[a] = (x + y)/ 2 -10;    // error since right hand side is Float type
                x = foo(a ,y);
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(arr),Id(a)),BinaryOp(-,BinaryOp(/,BinaryOp(+,Id(x),Id(y)),IntLiteral(2)),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_complex_array_index_expression_has_type_mismatch(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                a + b;
                return a;
            }
            void main(){
                int a[10], d[5];
                int x;
                float y;
                a[foo(x, y) + 2 /10 % 5];
                a[x * y - foo(x,y)];        //Error since x * y - foo(x,y) is float type not int
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,Id(x),Id(y)),CallExpr(Id(foo),[Id(x),Id(y)])))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_mix_all_expression(self):
        """More complex program"""
        input = """
            int[] foo(int a){
                int b[5];
                return b; 
            }
            void main(){
                int i[10], b[10], a [10];
                int c,d, x;
                (1 + 1*2 -3/4*5%6) == 2;        
                !true || !false != true;         
                i[1 *3 +4/2 - 5%1];              
                foo(2)[3+x] = a[b[2]] +3;        
                a[i[9] - b[3] + c - d] != b[12]; 
                foo(3)[true && false] == foo(2)[foo(3)[2] - true]; //Error since index can only be int type
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[IntLiteral(3)]),BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    # Statement checking
    def test_type_mismatch_in_if_statement(self):
        """More complex program"""
        input = """
            void main(){
                int a;
                float b;
                if(a == 0)
                    b + 1;
                
                if(b)
                    b + 1;
                }
        """
        expect = "Type Mismatch In Statement: If(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_mismatch_inside_if_else_statement(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                float b;
                boolean c;
                if(c)
                    b + 1;
                else
                    a + 2;
                
                
                if(b)       // Error
                    b + 1;
                else
                    b +2;    
            }
        """
        expect = "Type Mismatch In Statement: If(Id(b),BinaryOp(+,Id(b),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 456))

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
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_mismatch_in_simple_for_statement_expression_1(self):
        """More complex program"""
        input = """
            int a;
            float b;
            void main(){
                int c;
               for(c; c <a; c = c+1){ // Success
                    b = b+1;
               }
                for(b; c <a; c = c+1){ // Error
                    b = b+1;
               }
                foo(a,b);
            }
        """
        expect = "Type Mismatch In Statement: For(Id(b);BinaryOp(<,Id(c),Id(a));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_mismatch_in_simple_for_statement_expression_2(self):
        """More complex program"""
        input = """
            int a;
            float b;
            void main(){  
                int c;
               for(c; c == a; c = c+1){ // Success
                    b = b+1;
               }
                for(a; c = a; c = c+1){ // Error
                    b = b+1;
               }
            }
        """
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(=,Id(c),Id(a));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_mismatch_in_simple_for_statement_expression_3(self):
        """More complex program"""
        input = """
            int a;
            float b;
            void main(){
                 int c;
               for(c; c < a; c = c+1){ // Success
                    a = a+1;
                    c = c + 2;
               }
                for(c =0; c = a; b = b +1){ // Error
                    b = b+1;
               }
               return;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),Id(a));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_simple_return_wrong_type_statement(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                return b;
            }
            void main(){}
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_return_wrong_array_type(self):
        """More complex program"""
        input = """
            int[] goo(){
                int a[5];
                return a;
            }
            int[] goo1(){ 
                float b[5];
                return b; //Error
            }
            void main(){
                goo();
                goo1();
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_return_something_in_main_function(self):
        """More complex program"""
        input = """
            void main(){
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_type_mismatch_in_complex_if_statement(self):
        """More complex program"""
        input = """
           int main() {
            int i;
            if(i == 1){
                {
                i = 5;
                }
            }
            else {
                {
                if(i + 2)
                    i = 0;
                else 
                    i = i +1;
                }
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(i),IntLiteral(2)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_type_mismatch_in_complex_do_while(self):
        """More complex program"""
        input = """
            int main() {
                int i;
                int n;
                do{
                    n = n - 1;
                    i = i+1;
                    if( i ==n )
                        return i;
                    else
                        break;
                }
                while( i + n);      //Error
                }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(-,Id(n),IntLiteral(1))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),Id(n)),Return(Id(i)),Break())])],BinaryOp(+,Id(i),Id(n)))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_type_mismatch_in_complex_for_statement(self):
        """More complex program"""
        input = """int main() {
            int a,b,c,e;
            e = 9;
            for(a=1;a<=5;a=a+1)
             {
                for(b=0; b ;b= b+1)      // Error
                {
                    putIntLn(b);
                }
                putIntLn(a);
                e=e-2;
             }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(b),IntLiteral(0));Id(b);BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[Id(b)])]))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_complex_return_statement(self):
        """More complex program"""
        input = """
            int[] foo(int a){
                int b[5];
                return b;
            }
            int doo(int a, float b){
                return foo(2)[3+a];
            }
            boolean goo(int a, float b){
                return foo(4)[3+a];
            }
            void main(){ 
                int c;
                float d;
                doo(c,d);
                goo(c,d);
                return;
            }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(CallExpr(Id(foo),[IntLiteral(4)]),BinaryOp(+,IntLiteral(3),Id(a))))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_return_wrong_type_inside_if(self):
        """More complex program"""
        input = """
            int foo(){
                boolean a;
                if(a){
                    int b;
                    b = 1;
                    return b;
                }
                else{
                    float c;
                    c = 0;
                    return c;  //Error
                }

            }
            void main(){
                foo();
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_complex_program_with_mismatch_statement(self):
        """More complex program"""
        input = """
            void main(){ 
                if(true){
                    int i;
                    for(i = 0; i < 10; i = i +1){
                        do{
                            int e;
                            i + 2;
                        } while( i );  // Error
                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(e,IntType),BinaryOp(+,Id(i),IntLiteral(2))])],Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_complex_mismatch_type_return_extra_test(self):
        """More complex program"""
        input = """
            int[] foo(int a, int b[]){
                return b;
            }
            int foo1(int a){
                int c[5];
                return foo(a,c)[10]; 
            }
            float foo2(int a){
                return foo1(a); 
            }
             boolean foo3(int a){
                return foo1(a) == a;
            }
            boolean foo4(int a){
                return foo1(a) == foo2(a);  // Error
            }
            void main(){
                int a;
                foo3(a);
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(foo1),[Id(a)]),CallExpr(Id(foo2),[Id(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    # Test Break, continue
    def test_simple_break_inside_function(self):
        """More complex program"""
        input = """
            void main(){ 
                break;  //Error
                return;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_simple_continue_inside_function(self):
        """More complex program"""
        input = """
            void main(){ 
                continue;  //Error
                return;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_break_inside_if_not_in_loop(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                for( a = 0 ; a < 10; a = a+1){
                    if(a == 5){
                        break;
                    }
                }
                if(a == 5){
                        break; // Error
                }
                return;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_continue_inside_if_not_in_loop(self):
        """More complex program"""
        input = """
             void main(){ 
                int a;
                for( a = 0 ; a < 10; a = a+1){
                    if(a == 5){
                        continue;
                    }
                }
                if(a == 5){
                        continue; // Error
                }
                return;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_continue_break_inside_block_statement(self):
        """More complex program"""
        input = """
             void main(){ 
                {
                    {  
                        break;
                    }
                }
                return;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_complex_mix_continue_break(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                if( true){
                    for( a = 0 ; a < 10; a = a+1){
                        if(a == 5){
                            {
                            continue;
                            }
                        }
                        do
                            if(a < 9)
                                break;
                            else
                                continue;
                        while(a < 10);
                    }
                    break;      //Error
                }
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 476))

    # Test function not return
    def test_simple_not_return_function(self):
        """More complex program"""
        input = """
            int goo(){
                return 1;
            }
            int foo() {     //Error
                int a; 
            }
            void main(){ 
                foo();
            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_return_in_if(self):
        """More complex program"""
        input = """
            int goo(){
                if(true)
                    return 1;
                else
                    return 2;
            }
            int foo(){          //Error
                if(true)
                    return 1;
            }
            void main(){ 

            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_return_in_do_while(self):
        """More complex program"""
        input = """
            int goo(){
                do{
                    return 0;
                }
                while(true);
                
                return 1;
            }
            int foo(){      //Error
                do{
                    
                }
                while(true);
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_return_in_for(self):
        """More complex program"""
        input = """
            int foo(){
                int a;
                for(a = 0; a < 10; a = a+1){
                    return 1;
                }
                return 0;
            }
            int goo(){      //Error
                int a;
                for(a = 0; a < 10; a = a+1){
                    return 1;
                }
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function goo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_return_after_break_in_for_loop(self):
        """More complex program"""
        input = """
             int foo(){
                int a;
                for(a = 0; a < 10; a = a+1){
                    if( a == 5){
                        break;
                        return 1;
                    }
                }
                return 0;
            }
            int goo(){      //Error
                int a;
                for(a = 0; a < 10; a = a+1){
                    if( a == 5){
                        break;
                        return 1;
                    }
                }
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function goo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_return_after_continue_in_for_loop(self):
        """More complex program"""
        input = """
            int foo(){
                int a;
                for(a = 0; a < 10; a = a+1){
                    if( a == 5){
                        continue;
                        return 1;
                    }
                }
                return 0;
            }
            int goo(){      //Error
                int a;
                for(a = 0; a < 10; a = a+1){
                    if( a == 5){
                        continue;
                        return 1;
                    }
                }
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function goo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_no_return_in_loop(self):
        """More complex program"""
        input = """
            int foo(){ 
                int a;
                for(a = 0; a < 10; a = a+1){
                    if(true){
                        return 1;
                    }
                }
                return 1;
            }
            int doo(){      //Error
                int a;
                for(a = 0; a < 10; a = a+1){
                    if(true){
                        continue;
                    }
                }
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function doo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_return_after_break_in_do_while_loop(self):
        """More complex program"""
        input = """
            int foo() { 
                do
                    return 1;
                    break;
                while(false);
            }
            
            int goo(){          //Error
                do  
                    break;
                    return 1;   
                    
                while(false);
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function goo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_return_after_continue_in_do_while_loop(self):
        """More complex program"""
        input = """
            int foo() { 
                do
                    return 1;
                    continue;
                while(false);
            }
            
            int goo(){          //Error
                do  
                    continue;
                    return 1;   
                    
                while(false);
            }
            void main(){ 
                foo();
                goo();
            }
        """
        expect = "Function goo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_complex_function_no_return_error(self):
        """More complex program"""
        input = """
            int foo() { 
                int a;
                if(true) { 
                    { 
                        { 
                        return 2; 
                        } 
                    } 
                } 
                else 
                    for(a;a<3;a= a + 1) { 
                        return 1; 
                    } 
                }
            void main(){ 

            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_function_main_not_return(self):
        """More complex program"""
        input = """
             void foo(int a, float b){
                 foo(a,b);
             }
             int main(){
                 int a;
                 float b;
                 foo(a,b);
             }
         """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_complex_function_no_return_error_extra_test(self):
        """More complex program"""
        input = """
            int foo(int a, int b){
                int c;
                for(c = a; c < b; c = c + 1){
                    if(c == a/2){
                        return c;
                    }
                    else{
                        do{
                            c = c +1;
                        }
                        while(c < a/2 -1);
                        return c;
                    }
                }
            }
            void main(){ 

            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 488))

    # Test unreachable function
    def test_simple_reachable_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){ //Error
            }
            void main(){ 

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_unreachable_function_with_more_function(self):
        """More complex program"""
        input = """
            void doo(){}
            void foo(){
                doo();
            }
            void goo(int a, float b){ // Error
                foo();
            }
            void main(){ 
         
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_recursive_function_not_invoked(self):
        """More complex program"""
        input = """
               void foo(int a, float b){
                   foo(a,b);
               }
               void main(){

               }
           """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_complex_program_with_unreachable_function(self):
        """More complex program"""
        input = """
            void func1(){}
            void doo(){}
            void foo(){
                {
                    func1();
                }
            }
            void goo(int a, float b){ // Error
                doo();
                {
                        foo();
                }
            }
            void main(){ 
                func1();
                if(true){
                    foo();
                }
                else
                    doo();
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 492))

    # Test Not left value
    def test_simple_literal_on_left_side_of_assignment(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                a = 3;
                3 = a;
            }
        """
        expect = "Not Left Value: BinaryOp(=,IntLiteral(3),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_simple_binary_operation_on_left_side_of_assignment(self):
        """More complex program"""
        input = """
            void main(){ 
                int a;
                a = a +3;
                a + 3 =10;
            }
        """
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(3)),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_simple_unary_operation_on_left_side_of_assignment(self):
        """More complex program"""
        input = """
            void main(){ 
                float ace;
                ace = -1.5234;
                -ace = 1.5234;  //Error
            }
        """
        expect = "Not Left Value: BinaryOp(=,UnaryOp(-,Id(ace)),FloatLiteral(1.5234))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_call_expression_on_left_side_of_assignment(self):
        """More complex program"""
        input = """
            int foo(int a){
                return a*a;
            }
            void main(){
                int c, d[5];
                c = foo(10);
                d[4] = foo(5);
                foo(8) = c;
            }
        """
        expect = "Not Left Value: BinaryOp(=,CallExpr(Id(foo),[IntLiteral(8)]),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_check_mix_expression_on_left_side_of_assignment_expression(self):
        """More complex program"""
        input = """
            int[] foo(){
                int a[5];
                return a;
            }
            void main(){
                int a;
                a = 1+ 2 * 4 / 3 % 5;
                (a) = 3;
                foo()[4] = 2;
                (foo()[4] -a) = 1; //Error
            }
        """
        expect = "Not Left Value: BinaryOp(=,BinaryOp(-,ArrayCell(CallExpr(Id(foo),[]),IntLiteral(4)),Id(a)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    # CHECKING type mismatch - extra-check
    def test_swap_program_for_type_mismatch(self):
        """More complex program"""
        input = """
            void main(){
            int x , y , temp;
            x = 10;
            y =15;
            temp = x;
            x = y;
            y = temp;
            putString("x = %d and y = %d", x, y); //Error
        }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(putString),[StringLiteral(x = %d and y = %d),Id(x),Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_complex_program(self):
        """More complex program"""
        input = """
            int foo(int a, float b){
                if(a == 0){
                    if( b < 10){
                        do{
                            return 1;
                        }
                        while( a < 10);
                    }
                    else{
                        int i;
                        for(i = 0; i < b; i = i+1){
                            i = b/2 +i;         // Error
                        }
                    }
                }
                else{
                    do{
                        return 0;
                    }
                    while(a == 1);
                }
            }
            void main(){
                foo(1,1.5);
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(/,Id(b),IntLiteral(2)),Id(i)))"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_complex_program_has_type_mismatch(self):
        """More complex program"""
        input = """
            void main(){
                int a;
                a =0;
                if(true){
                    int a;
                    {
                        {
                        a =10;
                            {
                                do{
                                    a = a+ 1;
                                }while( a <100);
                            }
                        }
                    }
                }
                else{
                    for( a= 0; true; a = a+1){
                        if(a != 5){
                            float c;
                            c = a;
                            {
                                if( c % 2 != 0){ // Error
                                    return;
                                }
                            }
                        }
                        else{
                            {
                                continue;
                            }
                        }
                    }
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(c),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 500))

    # def test_complex_mismatch_type_return_extra_test_1(self):
    #     """More complex program"""
    #     input = """
    #     int pow(int pow) {
    #         return pow;
    #     }
    #
    #     void main() {
    #         pow(4);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(foo1),[Id(a)]),CallExpr(Id(foo2),[Id(a)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 501))
