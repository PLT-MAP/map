import ply.yacc as yacc
from MAPlexer import * 

#function declaration
def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN compound-statement'
	print "funtion-definition : {1} {2}{3}{4}{5}".format(t[0],t[1],t[2],t[3],t[4],t[5])
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5]

#identifiers
def p_id(t):
	'identifier : TEXT'
	print "identifier : {1}".format(t[0],t[1])
	t[0] = t[1]

#empty parameter list
def p_listE(t):
	'parameter-list : '

#multiple parameter list
def p_plist2(t):
	'parameter-list : parameter-list COMMA identifier'
	t[0]=t[1]+t[2]+t[3]

#single parameter
def p_plist(t):
	'parameter-list : identifier'
	t[0] = t[1]

#no compound statement
def p_cs_E(t):
	'compound-statement : '
	t[0] = ""

#compound statement
def p_cs(t):
	'compound-statement : LBR statement-list RBR'
	t[0] = t[1] + t[2] + t[3]

#single statement
def p_slist(t):
	'statement-list : statement'
	t[0] = t[1]
#multiple statements
def p_slist2(t):
	'statement-list : statement-list statement'

#no statements
def p_slist3(t):
	'statement-list : '
	t[0] = ""

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
#for tok in lexer:
	#print tok.type, tok.value

yacc.yacc()
#print 
yacc.parse(test)




