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


