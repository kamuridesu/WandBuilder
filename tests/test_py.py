import unittest
from main import Compiler
import pathlib
import os


class TestPython(unittest.TestCase):
    def test_hello(self):
        c = Compiler("py", "print('hello world')")
        to_compare = {'exit_code': '0', 'body': 'hello world\n'} 
        if c.postData():
            self.assertEqual(c.getResponse(), to_compare)
