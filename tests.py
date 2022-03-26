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


class testBash(unittest.TestCase):
    def test_hello(self):
        c = Compiler("sh", "echo \"hello world\"")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Bash")


class testCSharp(unittest.TestCase):
    def test_hello(self):
        c = Compiler("cs", "using System;\nclass MainClass {\n    static void Main() {\n        Console.WriteLine(\"hello world\");\n    }\n}")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="C#")


class testGO(unittest.TestCase):
    def test_hello(self):
        c = Compiler("go", "package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"hello world\")\n}")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="GO")


class testHaskell(unittest.TestCase):
    def test_hello(self):
        c = Compiler("haskell", "main = putStrLn \"hello world\"")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Haskell")


class testJulia(unittest.TestCase):
    def test_hello(self):
        c = Compiler("jl", "println(\"hello world\")")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Julia")


class testLua(unittest.TestCase):
    def test_hello(self):
        c = Compiler("lua", "print(\"hello world\")")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Lua")


class testPascal(unittest.TestCase):
    def test_hello(self):
        c = Compiler("pas", "program HelloWorld;\nbegin\n    writeln(\"hello world\")\nend.")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Pascal")


class testPerl(unittest.TestCase):
    def test_hello(self):
        c = Compiler("perl", "print \"hello world\\n\"")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Perl")


class testR(unittest.TestCase):
    def test_hello(self):
        c = Compiler("r", "cat(\"hello world\")")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="R")


class testRuby(unittest.TestCase):
    def test_hello(self):
        c = Compiler("rb", "puts \"hello world\"")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare, msg="Ruby")



if __name__ == '__main__':
    unittest.main()