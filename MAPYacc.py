import ply.yacc as yacc
from MAPlexer import * 
#parsing rules'

def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN compound-statement'
	#print "{0}:{1} {2} {3} {4}".format(t[1],t[2],t[3],t[4],t[5])

def p_id(t):
	'identifier : TEXT'
	t[0] = t[1]

def p_plist2(t):
	'parameter-list : parameter-list COMMA identifier'
	t[0]=t[1]+t[2]+t[3]

def p_plist(t):
	'parameter-list : identifier'
	t[0] = t[1]

<<<<<<< HEAD
#testing

def p_cs(t):
	'compound-statement : LBR statement-list RBR'
	t[0] = t[2]
	#print t[1], t[2], t[3]

def p_slist(t):
	'statement-list : statement'
	t[0] = t[1]

def p_slist2(t):
	'statement-list : statement-list statement'

#def p_s(t):
#	'statement : TEXT'
#	t[0] = t[1]
#	print t[0]

def p_s(t):
	'statement : aexpression'
	#| compound-statement
	#| selection-statement
	#| iteration-statement'''
	t[0] = t[1]

def p_expr(t):
	'aexpression : TEXT EQUALS NUMERIC'
	print t[1], t[2], t[3]

def p_error(t):
	print("Syntax error at '%s'" % t.value)
	print t[0]

test='func main(blah,poop,test){ poop=69 }'
=======
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
>>>>>>> 6510da4d4b9db5eda95415b464d20274b638b3a9
lexer=lex.lex()
lexer.input(test)
#for tok in lexer:
	#print tok.type, tok.value

yacc.yacc()
#print 
yacc.parse(test)




