import ply.yacc as yacc
from MAPlexer import * 
#parsing rules'

def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN' #compound-statement'
	print "{0}:{1} {2} {3} {4}".format(t[1],t[2],t[3],t[4],t[5])

def p_id(t):
	'identifier : TEXT'
	t[0] = t[1]

def p_plist2(t):
	'parameter-list : parameter-list COMMA identifier'
	t[0]=t[1]+t[2]+t[3]
	print t[0]

def p_plist(t):
	'parameter-list : identifier'
	t[0] = t[1]
	print t[0]

# better error message 
def p_error(t):
    if t is None:
        print "Syntax error: unexpected EOF"
    else:
        print "Syntax error at line {}: unexpected token {}".format(t.lineno, t.value)
    import inspect
    frame = inspect.currentframe()
    cvars = frame.f_back.f_locals
    print 'Expected:', ', '.join(cvars['actions'][cvars['state']].keys())
    print 'Found:', cvars['ltype']

test='func main(blah,test,  fun)'
lexer=lex.lex()
lexer.input(test)
for tok in lexer:
	print tok.type, tok.value

yacc.yacc()
#print 
yacc.parse(test)





