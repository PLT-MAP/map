import ply.lex as lex
from MAPlexer import *



test='100000 read() write()\n foreach'
lexer=lex.lex()
lexer.input(test)
for token in lexer:
	print lexer.token()














