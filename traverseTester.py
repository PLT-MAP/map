import string
import sys
import unittest
import yacc 
import MAPlexer 
import traverse 
from asciitree import *

sys.path.insert(0,'/path/test')
from MAPtestfiles import MapTests


class TestTraverseSyntax(unittest.TestCase):
	def setUp(self):
		self.lex=MAPlexer.MAPlex()

	def testlexer(self):
		self.assertEqual(self.lex.errored,False)

	def assert_prog(self, traversestring, expfile):
		teststr=expfile.read()
		teststr=teststr.splitlines()
		teststr=''.join(teststr)
		teststr=teststr.replace(" ", "")
		teststr=teststr.replace("\t", "")
		teststr=teststr.replace("\n", "") 
		#print teststr

		traversestring=traversestring.splitlines()
		traversestring=''.join(traversestring)
		traversestring=traversestring.replace(" ", "")
		traversestring=traversestring.replace("\t", "")
		traversestring=traversestring.replace("\n", "")
		#print traversestring
		
		self.assertEqual(teststr,traversestring)


	def testhelloworld(self):		 
		 test= MapTests.helloworld
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/helloworld.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	def testprintstatement(self):
		test= MapTests.print_statement
		m=yacc.MAPparser(self.lex,test)
		t=traverse.Traverse(m.ast)
		t.enter()
	def testifelsetest(self):
		test= MapTests.ifelsetest
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
			expfile=open("test/ifelsetest.txt",'r')
			self.assert_prog(t.complete(),expfile)

	def testifstatement(self):
		 test= MapTests.iftest
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/iftest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	
	def testifelifelsetest(self):
		 test= MapTests.ifelifelsetest
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/ifelifelsetest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	def testforstatement(self):
		test= MapTests.for_statement
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/forstatementtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	def testforeachstatement(self):
		test= MapTests.foreach_statement
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/foreachtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	def testnodeteststatement(self):
		test= MapTests.nodetest
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/nodetest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

	def testrwtest(self):
		test= MapTests.rwtest
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/rwtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
	def testsample1(self):
		test= MapTests.sample1
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample1.txt",'r')
		 	self.assert_prog(t.complete(),expfile)

if __name__ == "__main__": 
	unittest.main()
