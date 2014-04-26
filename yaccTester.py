import sys
import unittest
import yacc
import MAPlexer 
from MAPtestfiles import MapTests
from asciitree import *



class TestYaccSyntax(unittest.TestCase):

	def setUp(self):
		self.lex=MAPlexer.MAPlex()

	def testhelloworld(self):
		test= MapTests.helloworld
	#	print test
	#	result=yacc.MAPparser(self.lex,test)
	#	print draw_tree(result.ast)

	def testfunc(self):
		test= '''
		func main(Text hi) {
			if (5 < 7) {
				bye = 5;
				}
			}
		'''
		result=yacc.MAPparser(self.lex,test)
		print result
	#	print draw_tree(result.ast)
"""	def testarithmetic(self):
		test=  "func main(Text hi, Text bye) { Numeric n = 1+2;}"
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunc(self):
		test = "func main(Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore = 1; Text hello = 2; hello = oneMore + hello;}"
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunction(self):
		test=MapTests.graph
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunction1(self):
		test=MapTests.graphfile
	
		result=yacc.MAPparser(self.lex,test)
		print result
"""






if __name__ == "__main__": 
	unittest.main()
