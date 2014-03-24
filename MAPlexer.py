import ply.lex as lex
#http://flex.sourceforge.net/manual/Patterns.html
tokens = (
	
	'NUMERIC', #1
	'SINGLEQUOTE', #2
	'DOUBLEQUOTE', #2.1
	'TEXT',	   #3
	'BOOLEAN', #4
	'TIME',    #5	
	'NULL',    #6
	'DIREDGE', #7.1
	'UNDIREDGE', #7.2
	'NODE',    #8
	'PATH',    #9
	'GRAPH',   #10	
	'PLUS',    #11
	'MINUS',   #12
	'TIMES',   #13
	'DIVIDE',  #14
	'LPAREN',  #15
	'RPAREN',  #16
	'MODULUS', #16.1
	'LESSTHAN', #17
	'GREATERTHAN', #18
	'LESSTHANOREQUALTO', #19
	'GREATERTHANOREQUALTO', #20
	'EQUALSEQUALS', #21
	'DOESNOTEQUAL', #22	
	'ATSYM', #23
	'LOGICALAND', #24
	'LOGICALOR',  #25
	'COMMENT',    #26
	'COMMENTFRONT', #27
	'COMMENTBACK',   #28
	'PRINT',         #29
	#Graphing functions
	'GADD',          #30
	'GDELETE',       #31
	'GADJACENT',     #32
	'GPATH',         #33
	'GGETEDGE',      #34
	'GADDEDGE',      #35
	'GDELETEEDGE',   #35
	'GFINDSHORTESTPATH',#36
	'COMMA', #37
	'NEWLINE',#38
	'READ', #39
	'WRITE'#40
	'NEWLINE',#38

#keywords

	'FUNC',#39
	'LBR','RBR'


	)

#primitive data types
t_NUMERIC=r'(\d+\.?\d+)'   #1
t_SINGLEQUOTE=r'(\')' #2
t_DOUBLEQUOTE=r'(\")' #2.1
t_TEXT=r'[a-zA-Z]'+r'[a-zA-Z0-9]+'#3

def t_BOOLEAN(t): #4
	r'(True | False | true | false)'
	t.value='rue' in t.value
	return t

def t_TIME(t):
	r'Time'
	return t #5

def t_NULL(t):
	r'NULL' 
	t.value=None
	return t #6

def t_DIREDGE(t):
	r'Diredge' 
	return t #7.1
def t_UNDIREDGE(t):
	r'Undiredge'
	return t #7.2

def t_NODE(t):
	r'Node' 
	return t #8

def t_PATH(t):
	r'Path' 
	return t #9

def t_GRAPH(t):
	r'Graph' 
	return t  #10

#aritmetic operators
t_MODULUS = r'\%' #16.1
t_PLUS    = r'\+' #11
t_MINUS   = r'-'  #12
t_TIMES   = r'\*' #13
t_DIVIDE  = r'/'  #14
t_LPAREN  = r'\(' #15
t_RPAREN  = r'\)' #16
t_LESSTHAN=r'\<'  #17
t_GREATERTHAN=r'\>' #18
t_LESSTHANOREQUALTO=r'<\=' #19
t_GREATERTHANOREQUALTO=r'>\='#20
t_EQUALSEQUALS=r'=='#21
t_DOESNOTEQUAL=r'!='#22
t_ATSYM=r'\@'#23
t_LOGICALAND=r'&'  #24
t_LOGICALOR=r'\|'  #25

#commenting
t_COMMENT=r'//' #26
t_COMMENTBACK=r'(\*/)' #27
t_COMMENTFRONT=r'(/\*)'#28




#standard library operators
def t_PRINT(t):
	r'Print'         
	return t #29

t_GADD=r'\.add'          		#30
t_GDELETE=r'\.delete'       	#31
t_GADJACENT=r'\.adjacent'     	#32
t_GPATH=r'\.path'         		#33
t_GGETEDGE=r'\.getEdge'      	#34
t_GADDEDGE=r'\.addEdge'      	#35
t_GDELETEEDGE=r'\.deleteEdge'   #35
t_GFINDSHORTESTPATH=r'\.findShortestPath'   #36

t_COMMA=r'\,' #37
t_NEWLINE=r'\n'#38
def t_READ(t):
	r'read' 
	return t  #39
def t_WRITE(t):
	r'write' 
	return t  #40	


t_ignore  = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)



test='100000 read() write()\n'
lexer=lex.lex()
lexer.input(test)

print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()




#parsing rules

# Parsing rules

'''def p_tu_ed(t):
	'translation-unit : external-declaration'
	t[0] = t[1]

def p_tu_ed2(t):
	'translation-unit : translation-unit external-declaration'
	t[0] = t[1] + ' ' + t[2]

def p_ed1(t):
	'external-declaration : function-definition'
	t[0] = t[1]

def p_ed2(t):
	'external-declaration : statement'
	t[0] = t[1]
'''
def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN compound-statement'
	#t[0] = '{0}{1}{2}{3}{4}{5}'.format(t[1],t[2],t[3],t[4],t[5])

def p_id(t):
	'identifier : TEXT'
	t[0] = t[1]

def p_plist(t):
	'parameter-list : identifier'
	t[0] = t[1]

def p_plist2(t):
	'parameter-list : parameter-list COMMA identifier'
	t[0] = "{0}{1}{2}".format(t[1],t[2],t[3])

def p_cs(t):
	'compound-statement : LBR statement-list RBR'
	#	t[0] = "{0}{1}{2}{3}".format(t[1],t[2],t[3],t[4])

def p_slist(t):
	'statement-list : statement'
	t[0] = t[1]

def p_slist2(t):
	'statement-list : statement-list statement'
	#t[0] = "{0}{1}".format(t[1],t[2])

def p_slist3(t):
	'statement-list : '
	t[0] = ""
def p_s(t):
	'''statement : expression
	| compound-statement
	| selection-statement
	| iteration-statement'''
	t[0] = t[1]

def p_sels(t):
	'selection-statement : IF LPAREN expression RPAREN statement'

def p_sels2(t):
	'selection-statement : IF LPAREN expression RPAREN statement ELSE statement'

def p_iters(t):
	'iteration-statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'

def p_ters2(t):
	'iteration-statement : FOREACH LPAREN identifier IN identifier RPAREN statement'

def p_expr(t):
	'expression : assignment-expression'

def p_expr2(t):
	'expression : expression COMMA assignment-expression'

def p_aexpr(t):
	'assignment-expression : conditional-expression'

def p_aexpr2(t):
	'assignment-expression : primary-expression ASSIGN assignment-expression'

def p_condexpr(t):
	'''conditional-expression : logical-OR-expression
	| logical-AND-expression'''

def p_logorexpr(t):
	'logical-OR-expression : logical-AND-expression'

def p_logorexpr2(t):	
	'logical-OR-expression : logical-OR-expression | logical-AND-expression'

def p_logandexpr(t):
	'logical-AND-expression : equality-expression'

def p_logandexpr2(t):
	'logical-AND-expression : logical-AND-expression & equality-expression'

'''def p_incor(t):
	'inclusive-OR-expression : exclusive-OR-expression'

def p_incor2(t):
	'inclusive-OR-expression : exclusive-OR-expression | AND-expression'

def p_exor(t):
	'exclusive-OR-expression : AND-expression'

def p_exor2(t):
	'exclusive-OR-expression : exclusive-OR-expression ^ AND-expression'

def p_andexpr(t):
	'AND-expression : equality-expression'

def p_andexpr2(t):
	'AND-expression : AND-expression & equality-expression'
'''

def p_eqexpr(t):
	'equality-expression : relational-expression'

def p_eqexpr2(t):
	'''equality-expression : equality-expression == relational-expression
	| equality-expression != relational-expression'''

def p_relexpr(t):
	'relational-expression : additive-expression'

def p_relexpr2(t):
	'''relational-expression : relational-expression > additive-expression
	| relational-expression < additive-expression
	| relational-expression <= additive-expression
	| relational-expression >= additive-expression'''

def p_addexpr(t):
	'additive-expression : multiplicatve-exression'

def p_addexpr2(t):
	'''additive-expression : additive-expression PLUS multiplicative-expression
	| additive-expression MINUS multiplicative-expression'''

def p_multexpr(t):
	'multiplicative-expression : primary-expression'

def p_multexpr2(t):
	'''multiplicative-expression : multiplicative-expression STAR primary-expression
	| multiplicative-expression SLASH primary-expression'''

def p_primexp(t):
	'''primary-expression : identifier
	| constant
	| string
	| node
	| edge
	| LPAREN expression RPAREN
	| function-call'''

def p_funcall(t):
	'function-call : identifier DOT function-name LPAREN parameter-list RPAREN'

def p_funcall2(t):
	'''function-call : print LPAREN identifier RPAREN
	| read LPAREN identifier RPAREN
	| write LPAREN identifier COMMA identifier RPAREN'''

def p_funcname(t):
	'''function-name : 

def p_error(t):
	print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()
print yacc.parse("func main() {\n\tText t = \"Hello, world\";\n\tprint(t);\n}")


