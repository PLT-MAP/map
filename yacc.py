import ply.yacc as yacc
from MAPlexer import * 
from pprint import pprint

class Expr: pass

class Node(Expr):
	def __init__(self,name='',t='',children=[]):
		self.t = t
		self.children = children
		#print "children:" 
			
		#for i in self.children:
		#	print i
		
		self.name = name
		#print "name:{0}".format(self.name)


	def addChild(self,c):
		self.children.append(c)

	def __str__(self):
		return "{1}  {0}".format(self.name,self.t)
'''
	def __str__(self):
		ret = "^------" + repr(self.value) + repr(self.type) + "\n"
		
		if self.left is not None:
			ret += "^-----" + self.left.__str__() + "\n"
		
		if self.right is not None:
			ret += "^-----" + self.right.__str__() + "\n"
		
		return ret

	def __repr__(self):
		return '()'
'''
ast = Node('root') #root of the AST

def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN LBR statement-list RBR'
	t[0] = Node(t[2],'funcdef',[t[4],t[7]])
	global ast
	ast = t[0]

def p_id(t):
	'identifier : ID'
	t[0] = Node(t[1])

def p_listE(t):
	'parameter-list : '
	t[0] = Node()

def p_plist(t):
	'parameter-list : type-declaration'
	t[0] = Node('','param-list',[t[1]])

def p_plist2(t):
	'parameter-list : parameter-list COMMA type-declaration'
	t[0] = Node(t[2],'param-list',[t[1],t[3]])

def p_typedec(t):
	'type-declaration : TYPE identifier'
	t[0] = Node(t[1],'typedec',[t[2]])

def p_slist2(t):
	'statement-list : statement-list statement'
	t[0] = Node('','statement-list',[t[1],t[2]])
	
def p_slist(t):
	'statement-list : statement SEMICOLON'
	t[0] = Node(t[2],'statement-list',[t[1]])

def p_slist3(t):
	'statement-list : '
	t[0] = Node()

def p_s(t):
	'''statement : expression
	| function-call'''
	t[0] = Node('','statement',[t[1]])

'''| selection-statement
| iteration-statement'''

#if statement
def p_sels(t):
	'selection-statement : IF LPAREN expression RPAREN statement'
	t[0] = Node(t[1],'selection-statement',[t[3],t[5]])

#else statement
def p_sels2(t):
	'selection-statement : IF LPAREN expression RPAREN statement ELSE statement'
	t[0] = Node(t[1],'selection-statement',[t[3],t[5],t[7]])


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
	t[0] = Node('','expr',[t[1]])

#Conditional expression
def p_aexpr(t):
	'assignment-expression : conditional-expression'
	t[0] = Node('','assignment-expression',[t[1]])

def p_aexpr2(t):
	'assignment-expression : primary-expression EQUALS assignment-expression'
	t[0] = Node(t[2],'assignment-expression',[t[1],t[3]])

def p_condexpr(t):
	'''conditional-expression : logical-OR-expression
	| logical-AND-expression'''
	t[0] = Node('','conditional-expression',[t[1]])

def p_logorexpr(t):
	'logical-OR-expression : logical-AND-expression'
	t[0] = Node('','logical-or-expr',[t[1]])

def p_logorexpr2(t):	
	'logical-OR-expression : logical-OR-expression LOGICALOR logical-AND-expression'
	t[0] = Node(t[2],'',[t[1],t[3]])

def p_logandexpr(t):
	'logical-AND-expression : equality-expression'
	t[0] = Node('','logical-and-expr',[t[1]])

def p_logandexpr2(t):
	'logical-AND-expression : logical-AND-expression LOGICALAND equality-expression'
	t[0] = Node(t[2],'logical-and-expr',[t[1],t[3]])

def p_eqexpr(t):
	'equality-expression : relational-expression'
	t[0] = Node('','equality-expression',[t[1]])

def p_eqexpr2(t):
	'''equality-expression : equality-expression EQUALSEQUALS relational-expression
	| equality-expression DOESNOTEQUAL relational-expression'''
	t[0] = Node(t[2],'equality-expression',[t[1],t[3]])

def p_relexpr(t):
	'relational-expression : additive-expression'
	t[0] = Node('','relational-expression',[t[1]])

def p_relexpr2(t):
	'''relational-expression : relational-expression GREATERTHAN additive-expression
	| relational-expression LESSTHAN additive-expression
	| relational-expression LESSTHANOREQUALTO additive-expression
	| relational-expression GREATERTHANOREQUALTO additive-expression'''
	t[0] = Node(t[2],'relational-expression',[t[2],t[3]])

def p_addexpr(t):
	'additive-expression : multiplicative-expression'
	t[0] = Node('','additive-expression',[t[1]])

def p_addexpr2(t):
	'''additive-expression : additive-expression PLUS multiplicative-expression
	| additive-expression MINUS multiplicative-expression'''
	t[0] = Node(t[2],'additive-expression', [t[1],t[3]])

def p_multexpr(t):
	'multiplicative-expression : primary-expression'
	t[0] = Node('','multiplicative-expression',[t[1]])

def p_multexpr2(t):
	'''multiplicative-expression : multiplicative-expression TIMES primary-expression
	| multiplicative-expression DIVIDE primary-expression'''
	t[0] = Node(t[2],'multiplicative-expression',[t[1], t[3]])

def p_primexp(t):
	'''primary-expression : identifier
	| type-declaration
	| LITERAL
	| NUMERIC'''
	t[0] = Node('','primary-expression',[t[1]])

def p_primexp2(t):
	'''primary-expression : LPAREN expression RPAREN'''	
	t[0] = Node('','primary-expression', [t[2]])

def p_funcall(t):
	'function-call : identifier PERIOD function-name LPAREN parameter-list RPAREN'
	t[0] = Node(t[2],'function-call',[t[1],t[3],t[5]])

def p_funcall2(t):
	'function-call : identifier LPAREN func-args RPAREN'
	t[0] = Node('','function-call',[t[1], t[3]])

def p_funcargs(t):
	'func-args : arg'
	t[0] = Node('','func-args',[t[1]])

def p_funcargs2(t):
	'func-args : func-args COMMA arg'
	t[0] = Node(t[2],[t[1],t[3]])

def p_arg(t):
	'''arg : LITERAL
	| identifier'''
	t[0] = Node('','arg',[t[1]])

def p_arg_E(t):
	'arg : '
	t[0] = Node()

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
	t[0] = Node('','function-name',[t[1]])

#i = "func main(Text hi, Text bye) { Numeric n = 1+2;}"
#i = "func main(Text hi, Numeric bye) {print(hi);}"
#i = "func main(Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2}"
i = "func main(Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore; }"

def p_error(t):
	import inspect
	frame = inspect.currentframe()
	cvars = frame.f_back.f_locals
	#pprint (cvars)
	print "SYNTAX ERROR:"
	print 'Expected:', ', '.join(cvars['actions'][cvars['state']].keys())
	print 'Found:', cvars['ltype']
	print 'Errtoken: {0}'.format(cvars['errtoken'])
	print "input: {0}".format(i)

l = lex.lex()
lex.input(i)

while 1:
	tok = lex.token()
	if not tok: break
	#print tok

yacc.yacc()
yacc.parse(i,lexer=l,tracking=True)





