import ply.lex as lex
from MAPlexer import *



test='100000 read()'
lexer=lex.lex()
lexer.input(test)

for tok in lexer:
	print tok.type, tok.value








