import ply.lex as lex
from MAPlexer import *


#put any input you want to test here
###############################################
test='.0821 100000 read()[] {} = == // . !! : ' 
lexer=lex.lex()
lexer.input(test)

for tok in lexer:
	print tok.type, tok.value
###############################################



