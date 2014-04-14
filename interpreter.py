from yacc import *
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



m = mapparser("func main(Text hi){Text hi = 'bye';}")
print draw_tree(m.ast)

