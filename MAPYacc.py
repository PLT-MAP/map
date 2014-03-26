import ply.yacc as yacc
from MAPlexer import * 
#parsing rules'

#def p_fd(t):
#	'function-definition : FUNC identifier LPAREN parameter-list RPAREN' #compound-statement'

def p_id(t):
	'identifier : TEXT'
	t[0] = t[1]

def p_error(t):
	print("Syntax error at '%s'" % t.value)

test='poop'
yacc.yacc()
print yacc.parse(test)




