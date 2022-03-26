import unittest
from main import Compiler
import pathlib
import os


class TestPython(unittest.TestCase):
    def test_hello(self):
        c = Compiler("py", "print('hello world')")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Python")


class testC(unittest.TestCase):
    def test_hello(self):
        c = Compiler("c", "#include <stdio.h>\nint main() {\n    printf(\"hello world\\n\");\n    return 0;\n}\n")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="C")


class testJava(unittest.TestCase):
    def test_hello(self):
        c = Compiler("java", "class Main {\n    public static void main(String[] args) {\n        System.out.println(\"hello world\");\n    }\n}")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Java")


class testCpp(unittest.TestCase):
    def test_hello(self):
        c = Compiler("cPP", "#include <iostring>\nint main() {\n    cout << \"hello world\n\";\n    return 0;\n}\n")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="C++")


class testJs(unittest.TestCase):
    def test_hello(self):
        c = Compiler("js", "console.log(\"hello world\");")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="JavaScript")


class testPHP(unittest.TestCase):
    def test_hello(self):
        c = Compiler("php", "<?php echo \"hello world\n\" ?>")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="PHP")


class testRust(unittest.TestCase):
    def test_hello(self):
        c = Compiler("rust", "fn main() {\n    println!(\"hello world\");\n}")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Rust")


class testTyescript(unittest.TestCase):
    def test_hello(self):
        c = Compiler("ts", "console.log(\"hello world\");")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Typescript")



if __name__ == '__main__':
    unittest.main()