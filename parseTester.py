import ply.lex as lex
from MAPlexer import *


#put any input you want to test here
test='return read() continue else1 .0821 100000 = Graph( read()[] {} = == func1 in  return1' 
lexer=lex.lex()
lexer.input(test)

for tok in lexer:
	print tok.type, tok.value


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

	test='\''
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='SINGLEQUOTE':
			print "Test3 failed"
			return False

	print "Test3 passed"

	test='piPrint Printpo d1234537 piread readpi piwrite writepi piNode Nodepi Pathdh laPath piGraph Graphpo poforeach foreach39 tif fitif tofor winterbreak breakfast Timer PiTime PUndiredge Undiredge12 Diredge1 diDiredge internet pin elserpoop pesle klcontinue continuefdjj func1 else1 returnies forpeach fort break1 a12true b1092false elseif Timey NULLMASTER5000'
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='TEXT':
			print "Test4 failed"
			return False
	print "Test4 passed"

	test='True False'
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='BOOLEAN':
			print "Test5 failed"
			return False

	print "Test5 passed"	

	test='Time Time Time Time'
	lexer=lex.lex()
	lexer.input(test)
	for tok in lexer:
		if tok.type!='TIME':
			print "Test6 failed"
			return False

	print "Test6 passed"	




testlex()




