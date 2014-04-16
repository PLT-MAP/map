from yacc import * 
from MAPlexer import *
from asciitree import *


def walkAst(t,state={}):
	
	#print "visiting node: >>{0}<<".format(t)

	#check types in arithmetic operations

	if state.get('processingAdditiveExpression') == 1:
		print t
	elif t.type == 'additive-expression':# or childTypeIs('additive-expression'):
		print t
		state['processingAdditiveExpression'] = 1

	
	for n in t.children:
		walkAst(n,state)
	
	state['processingAdditiveExpression'] = 0

i = "func main(Text hi,Numeric NumericArg, Graph GraphArg, Path PathArg, Node NodeArg) {Text hi = 'bye';}"
l = MAPlex()
l.input = i
l.tokenize(i)
m = MAPparser(l,i)
print draw_tree(m.ast)

