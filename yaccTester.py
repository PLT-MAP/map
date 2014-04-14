import sys
import unittest
from yacc import *
from MAPlexer import *



class TestYaccSyntax(unittest.TestCase):
	def setUp(self):
		self.parser=yacc.yacc()
		lexer = lex.lex()

	def testhelloworld(self):
		 test= "func main(Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2}"
		 result=self.parser.parse(test,lexer=lexer,tracking=True)
		 print result

	def testprintfunc(self):
		 test= "func main(Text hi, Numeric bye) {print(hi);}"
		 result=self.parser.parse(test,lexer=lexer,tracking=True)
		 print result

	def testarithmetic(self):
		 test=  "func main(Text hi, Text bye) { Numeric n = 1+2;}"
		 result=self.parser.parse(test,lexer=lexer,tracking=True)
		 print result
	def testgraphfunc(self):
		test = "func main(Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore = 1; Text hello = 2; hello = oneMore + hello;}"
		result=self.parser.parse(test,lexer=lexer,tracking=True)
		print result		



if __name__ == "__main__": 
	unittest.main()