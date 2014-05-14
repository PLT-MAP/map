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
		 print "Testing helloworld:"
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/helloworld.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test hello world: Passed"

	def testprintstatement(self):
		test= MapTests.print_statement
		print "Testing print statements:"
		m=yacc.MAPparser(self.lex,test)
		t=traverse.Traverse(m.ast)
		t.enter()
		print "Test print statement: Passed" 

	def testifelsetest(self):
		test= MapTests.ifelsetest
		print "Testing if and else statements:"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
			expfile=open("test/ifelsetest.txt",'r')
			self.assert_prog(t.complete(),expfile)
			print "Test if else test: Passed" 
	def testifstatement(self):
		 test= MapTests.iftest
		 print "Testing if statements:"
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/iftest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test if statement: Passed" 

	def testifelifelsetest(self):
		 test= MapTests.ifelifelsetest
		 print "testing if elif else statements:"
		 m=yacc.MAPparser(self.lex,test)
		 self.assertEquals(m.errored,False)
		 if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/ifelifelsetest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test if elif else test: Passed" 

	def testforstatement(self):
		test= MapTests.for_statement
		print "Testing for statements:"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/forstatementtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test for statement: Passed" 
	
	def testforeachstatement(self):
		test= MapTests.foreach_statement
		print "Testing for each statements:"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/foreachtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test for each statement: Passed" 



	def testnodeteststatement(self):
		print "Test nodes:"
		test= MapTests.nodetest
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/nodetest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test simple node: Passed" 
	
	def testrwtest(self):
		test= MapTests.rwtest
		print "Test read and write:"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/rwtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test read and writing: Passed" 

	def testpathtest(self):
		test= MapTests.pathtest
		print "testing paths:"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/pathtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test building path: Path" 
	
	def testsample1(self):
		print "testing sample program #1"
		test= MapTests.sample1
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample1.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 1: Passed" 

	def testsample2(self):
		test= MapTests.sample2
		print "Testing sample program #2" 
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample2.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 2: Passed" 
	
	def testsample3(self):
		test= MapTests.sample3
		print "Testing sample program #3"
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample3.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 3: Passed" 

	def testsample4(self):
		print "Testing sample program #4"
		test= MapTests.sample4
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample4.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 4: Passed" 

	def testsample5(self):
		print "Testing sample program #5"
		test= MapTests.sample5
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample5.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 5: Passed" 

	def testsample6(self):
		print "Testing sample program #6"
		test= MapTests.sample6
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/sample6.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test sample program 6: Passed" 

	def testshortestpath(self):
		print "Testing shortest path"
		test= MapTests.shortestPathtest
		m=yacc.MAPparser(self.lex,test)
		self.assertEquals(m.errored,False)
		if not m.errored:
			t=traverse.Traverse(m.ast)
		 	expfile=open("test/shortestPathtest.txt",'r')
		 	self.assert_prog(t.complete(),expfile)
			print "Test shortest path test: Passed"  

if __name__ == "__main__": 
	print "BEGIN TRAVERSE TEST"
	print "-------------------"
	unittest.main()
