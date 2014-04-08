from yacc import *
from asciitree import *


def walkAst(t):
	
	print "visiting node: >>{0}<<".format(t)

	if t.left is not None:
		walkAst(t.left)
	if t.right is not None:
		walkAst(t.right)

print draw_tree(ast)

