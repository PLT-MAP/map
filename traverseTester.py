import string
import sys
import unittest
import yacc 
import MAPlexer 
import traverse 
from MAPtestfiles import MapTests
from asciitree import *


class TestTraverseSyntax(unittest.TestCase):
	def setUp(self):
		self.lex=MAPlexer.MAPlex()

	def assert_lexer(self):
		self.assertEqual(self.lex.errored,False)


	def assert_prog(self, traversestring, expfile):
		teststr=expfile.read()
		teststr=teststr.splitlines()
		teststr=''.join(teststr)
		teststr=teststr.replace(" ", "")
		teststr=teststr.replace("\t", "")
		teststr=teststr.replace("\n", "") 
		print teststr

		traversestring=traversestring.splitlines()
		traversestring=''.join(traversestring)
		traversestring=traversestring.replace(" ", "")
		traversestring=traversestring.replace("\t", "")
		traversestring=traversestring.replace("\n", "")
		print traversestring
		
		self.assertEqual(teststr,traversestring)


	def testhelloworld(self):
		 test= MapTests.helloworld
		 m=yacc.MAPparser(self.lex,test)
		 t=traverse.Traverse(m.ast)
		 self.assertEquals(m.errored,False)
		 expfile=open("test/helloworld.txt",'r')
		 self.assert_prog(t.complete(),expfile)

	def testprintstatement(self):
		 test= MapTests.print_statement
		 m=yacc.MAPparser(self.lex,test)
		 t=traverse.Traverse(m.ast)
		 t.enter()

"""

	def testifstatement(self):
		 test= MapTests.if_statement
		 m=yacc.MAPparser(self.lex,test)
		 t=traverse.Traverse(m.ast)
		 t.enter()

	def testifelsestatement(self):
                 test= MapTests.ifelse_statement
                 m=yacc.MAPparser(self.lex,test)
                 t=traverse.Traverse(m.ast)
                 t.enter()	
	def testifelifelsestatement(self):
                 test= MapTests.ifelifelse_statement
                 m=yacc.MAPparser(self.lex,test)
                 t=traverse.Traverse(m.ast)
                 t.enter()
	def testforstatement(self):
                 test= MapTests.for_statement
                 m=yacc.MAPparser(self.lex,test)
                 t=traverse.Traverse(m.ast)
                 t.enter()
	def testforeachstatement(self):
                 test= MapTests.foreach_statement
                 m=yacc.MAPparser(self.lex,test)
                 t=traverse.Traverse(m.ast)
                 t.enter()
"""
if __name__ == "__main__": 
	unittest.main()
