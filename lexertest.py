import unittest
import MAPlexer 
from MAPtestfiles import MapTests



class TestLexingSyntax(unittest.TestCase):
	
	def setUp(self):
		self.lex=MAPlexer.MAPlex()
		self.lex.build()
		self.lexer=self.lex.lexer

	def test_tokens(self):
		print "Testing all tokens:"
		cases={
		#'\"':'DOUBLEQUOTE', 
		'piNULLdel':'ID',	   
		'1':'NUMERIC',
		'1234':'NUMERIC',
		'.01231':'NUMERIC',
		'12312.213123':'NUMERIC',
		'null':'NULL',
		'include':'INCLUDE',
		'true' : 'BOOLEAN', 
		'false' : 'BOOLEAN',
		'Time':'TIME',
		#'DirEdge':'DIREDGE',
		#'UndirEdge':'UNDIREDGE',
#		'print':'PRINT', 
		'add':'ADD',
		'delete':'DELETEFUNC',
		'path':'PATHFUNC',
		'adjacent':'ADJACENTFUNC',
		'getEdge':'GETEDGEFUNC',
		'addEdge':'ADDEDGEFUNC',
		'deleteEdge':'DELETEEDGEFUNC',
		'findShortest':'FINDSHORTESTFUNC',
		'equals':'EQUALSFUNC',
		'in':'IN',
		'if':'IF', 
		'for':'FOR', 
		'break':'BREAK', 
		'elif':'ELIF', 
		'foreach':'FOREACH',
		'continue':'CONTINUE',
		'return':'RETURN',
		'else':'ELSE', 
		'read':'READ', 
		'write':'WRITE',
		'func':'FUNC',
		'Node':'TYPE',
		'Path':'TYPE',
		'Graph':'TYPE',
		'Text':'TYPE',
		'Numeric':'TYPE'
		}
		self.assert_tokens_eq(cases)
		print "Token test passed!"

	def assert_tokens_eq(self,cases):
		for key, val in cases.iteritems():
			self.lexer.input(str(key))
			token = self.lexer.token()
			print "asserting key: " + key
			#self.assertEqual(key, token.value) 
			self.assertEqual(val, token.type)

	def test_hello_world_eq(self):
		print "Asserting syntax of hello world and checking generated tokens:"
		self.lexer.input("func main(Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2;}")
		#self.lexer.input(MapTests.helloworld)
		#progfile = open('testfiles/helloworld.map', 'r')
		token = self.lexer.token()
		self.assertEqual('FUNC', token.type)
		token = self.lexer.token()
		self.assertEqual('ID', token.type)
		token = self.lexer.token()
		self.assertEqual('LPAREN', token.type)
		token = self.lexer.token()
		self.assertEqual('TYPE', token.type)
		token = self.lexer.token()
		self.assertEqual('ID', token.type)
		token = self.lexer.token()
		self.assertEqual('COMMA', token.type)
		token = self.lexer.token()
		self.assertEqual('TYPE', token.type)
		token = self.lexer.token()
		self.assertEqual('ID', token.type)
		token = self.lexer.token()
		self.assertEqual('RPAREN', token.type)
		token = self.lexer.token()
		self.assertEqual('LBR', token.type)
		token = self.lexer.token()
		self.assertEqual('TYPE', token.type)
		token = self.lexer.token()
		self.assertEqual('ID', token.type)
		token = self.lexer.token()
		self.assertEqual('EQUALS', token.type)
		token = self.lexer.token()
		self.assertEqual('LITERAL', token.type)
		token = self.lexer.token()
		self.assertEqual('SEMICOLON', token.type)
		token = self.lexer.token()
		self.assertEqual('ID', token.type)
		token = self.lexer.token()
		self.assertEqual('EQUALS', token.type)
		token = self.lexer.token()
		self.assertEqual('NUMERIC', token.type)
		token = self.lexer.token()
		self.assertEqual('SEMICOLON', token.type)
		token = self.lexer.token()
		self.assertEqual('RBR', token.type)
		print "Hello world test passed!"
		print



if __name__ == "__main__": 
	unittest.main()




