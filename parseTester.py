import ply.lex as lex
from MAPlexer import *


#Sandya, put any input you want to test here
###############################################
test=''
lexer=lex.lex()
lexer.input(test)

for tok in lexer:
	print tok.type, tok.value
###############################################

def testlex():
	#tester to make sure that the tokens work
	
	#check numeric
	test='10 10.5 10.9 1000000 2138920183 102.202 .02931'
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='NUMERIC':
			print "Test1 failed"
			return False
	print "Test1 passed"

	test='""""""""""""""'
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='DOUBLEQUOTE':
			print "Test2 failed"
			return False

	print "Test2 passed"






testlex()




