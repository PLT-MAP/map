import ply.yacc as yacc
from MAPlexer import * 
from pprint import pprint

#function definition
def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN LBR statement-list RBR'
	print "funtion-definition : {1} {2} {3} {4} {5}".format(t[0],t[1],t[2],t[3],t[4],t[5])
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5]

#identifiers
def p_id(t):
	'identifier : ID'
	print "identifier : {1}".format(t[0],t[1])
	t[0] = t[1]

#parameter list
def p_listE(t):
	'parameter-list : '
	pass

def p_plist(t):
	'parameter-list : type-declaration'
	t[0] = t[1]
	print "parameter-list : {0}".format(t[1])

def p_plist2(t):
	'parameter-list : parameter-list COMMA type-declaration'
	t[0] = t[1] + t[2] + t[3]
	print "parameter-list : {0} {1} {2}".format(t[1],t[2],t[3])
'''
#Body of a function
def p_cs(t):
	'compound-statement : LBR statement-list RBR'
	t[0] = t[1] + t[2] + t[3]
	print "compound-statement : {0} {1} {2}".format(t[1],t[2],t[3])

def p_cs_E(t):
	'compound-statement : '
	t[0] = ""
'''
#group of statements

def p_slist2(t):
	'statement-list : statement-list SEMICOLON statement'
	t[0] = t[1] + t[2] + t[3]

def p_slist(t):
	'statement-list : statement SEMICOLON'
	t[0] = t[1] + t[2]
	print "statement-list : {0} {1}".format(t[1],t[2])

def p_slist3(t):
	'statement-list : '
	pass

#Statements
def p_s(t):
	'''statement : expression
	| function-call'''
	t[0] = t[1]

'''| selection-statement
| iteration-statement'''

#if statement
def p_sels(t):
	'selection-statement : IF LPAREN expression RPAREN statement'
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5]

#else statement
def p_sels2(t):
	'selection-statement : IF LPAREN expression RPAREN statement ELSE statement'
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7]

'''
#for loop
def p_iters(t):
	'iteration-statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement' #compound-statement?
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7] + t[8] + t[9]

#foreach
def p_ters2(t):
	'iteration-statement : FOREACH LPAREN identifier IN identifier RPAREN statement' #compound-statement
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7]'''

#assignment
def p_expr(t):
	'expression : assignment-expression'
	t[0] = t[1]

#Conditional expression
def p_aexpr(t):
	'assignment-expression : conditional-expression'
	t[0] = t[1]
def p_aexpr2(t):
	'assignment-expression : primary-expression EQUALS assignment-expression'
	t[0] = t[1] + t[2] + t[3] 

def p_condexpr(t):
	'''conditional-expression : logical-OR-expression
	| logical-AND-expression'''
	t[0] = t[1]

def p_logorexpr(t):
	'logical-OR-expression : logical-AND-expression'
	t[0] = t[1]

def p_logorexpr2(t):	
	'logical-OR-expression : logical-OR-expression LOGICALOR logical-AND-expression'
	t[0] = t[1] + t[2] + t[3]

def p_logandexpr(t):
	'logical-AND-expression : equality-expression'
	t[0] = t[1]

def p_logandexpr2(t):
	'logical-AND-expression : logical-AND-expression LOGICALAND equality-expression'
	t[0] = t[1] + t[2] + t[3]

def p_eqexpr(t):
	'equality-expression : relational-expression'
	t[0] = t[1]

def p_eqexpr2(t):
	'''equality-expression : equality-expression EQUALSEQUALS relational-expression
	| equality-expression DOESNOTEQUAL relational-expression'''
	t[0] = t[1] + t[2] + t[3]

def p_relexpr(t):
	'relational-expression : additive-expression'
	t[0] = t[1]

def p_relexpr2(t):
	'''relational-expression : relational-expression GREATERTHAN additive-expression
	| relational-expression LESSTHAN additive-expression
	| relational-expression LESSTHANOREQUALTO additive-expression
	| relational-expression GREATERTHANOREQUALTO additive-expression'''
	t[0] = t[1] + t[2] + t[3]

def p_addexpr(t):
	'additive-expression : multiplicative-expression'
	t[0] = t[1]

def p_addexpr2(t):
	'''additive-expression : additive-expression PLUS multiplicative-expression
	| additive-expression MINUS multiplicative-expression'''
	t[0] = t[1] + t[2] + t[3]

def p_multexpr(t):
	'multiplicative-expression : primary-expression'
	t[0] = t[1]

def p_multexpr2(t):
	'''multiplicative-expression : multiplicative-expression TIMES primary-expression
	| multiplicative-expression DIVIDE primary-expression'''
	t[0] = t[1] + t[2] + t[3]

def p_primexp(t):
	'''primary-expression : identifier
	| type-declaration
	| LITERAL'''
	t[0] = t[1]

def p_typedec(t):
	'type-declaration : TYPE identifier'
	t[0] = t[1] + t[2]
	print "type-declaration : {0} {1}".format(t[1],t[2])

def p_primexp2(t):
	'''primary-expression : LPAREN expression RPAREN'''	
	t[0] = t[1] + t[2] + t[3]

def p_funcall(t):
	'function-call : identifier PERIOD function-name LPAREN parameter-list RPAREN'
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6]

def p_funcall2(t):
	'function-call : identifier LPAREN func-args RPAREN'
	t[0] = t[1] + t[2] + t[3] + t[4]

def p_funcargs(t):
	'func-args : arg'
	t[0] = t[1]

def p_funcargs2(t):
	'func-args : func-args COMMA arg'
	t[0] = t[1] + t[2] + t[3]

def p_arg(t):
	'''arg : LITERAL
	| identifier'''
	t[0] = t[1]

def p_arg_E(t):
	'arg : '
	pass
'''
def p_funcall2(t):
	function-call : PRINT LPAREN identifier RPAREN
	| READ LPAREN identifier RPAREN
	| WRITE LPAREN identifier COMMA identifier RPAREN
	t[0] = t[1] + t[2] + t[3] + t[4]
'''

def p_funcname(t):
	'''function-name : ADD
	| DELETEFUNC
	| ADJACENTFUNC
	| PATHFUNC
	| GETEDGEFUNC
	| ADDEDGEFUNC
	| DELETEEDGEFUNC
	| FINDSHORTESTFUNC
	| EQUALSFUNC'''
	t[0] = t[1]
	print "function-name : {0}".format(t[1])

def p_error(t):
    import inspect
    frame = inspect.currentframe()
    cvars = frame.f_back.f_locals
    print 'Expected:', ', '.join(cvars['actions'][cvars['state']].keys())
    print 'Found:', cvars['ltype']

l = lex.lex()
i = "func main(hi, bye) { Numeric n = 1+2;}"
lex.input(i)

while 1:
	tok = lex.token()
	if not tok: break
	print tok

yacc.yacc()
yacc.parse(i,lexer=l)


#print yacc.parse("func main(Text hi, Numeric bye) {print(hi);}")
#print yacc.parse("func main(Text hi, Numeric bye) { Text t = 'Hello, world';}")
#print yacc.parse("func main(hi, bye) { Numeric n = 1+2;}")


