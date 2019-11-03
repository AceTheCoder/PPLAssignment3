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

    def test_wrong_main_function_type(self):
        """More complex program"""
        input = """float main(){}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_redeclare_function_name(self):
        """More complex program"""
        input = """
        int main(){}
        int foo() {
            putIntLn(getInt());
        }
        float foo(){
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_global_variable(self):
        """Simple program: int main() {} """
        input = """int a;
        float a;
        int main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_global_array(self):
        """Simple program: int main() {} """
        input = """int a[5];
        float a;
        int main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_global_array_function(self):
        """Simple program: int main() {} """
        input = """int[] foo(){}
        float[] foo(){}
        int main(){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_mix_global_declaration(self):
        """Simple program: int main() {} """
        input = """int a,b,c;
        void foo(){}
        string a;
        int foo(){}
        int main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_parameter(self):
        """More complex program"""
        input = """
            int a;
            int foo(float b, string b){
            }
            int main(){}
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_parameter_inside_function(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                string b;
            }
            int main(){}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test(self):
        """More complex program"""
        input = """
            void foo(int a, float b){
                 putIntLn(c);
            }
            int main(){}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 409))
    