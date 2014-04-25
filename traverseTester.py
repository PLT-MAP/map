import sys
import unittest
import yacc 
import MAPlexer 
import traverse 
from MAPtestfiles import MapTests


class TestTraverseSyntax(unittest.TestCase):
	def setUp(self):
		self.parser=yacc.MAPparser
		self.lex=MAPlexer.MAPlex()

	def testhelloworld(self):
		 test= MapTests.helloworld
		 m=self.parser(self.lex,test)
		 print traverse.draw_tree(m.ast)
		 #t=traverse.Traverse(self,m.ast)
		 #t.enter()


if __name__ == "__main__": 
	unittest.main()