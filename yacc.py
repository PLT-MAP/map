import ply.yacc as yacc
from MAPlexer import * 
from pprint import pprint

class Expr: pass

class Node(Expr):
	def __init__(self,name='',type='',children=None,leaf=None,token=None):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = []
		#print "children:" 
			
		#for i in self.children:
		#	print i
		self.leaf = leaf
		self.token = token
		self.name = name
		#print "name:{0}".format(self.name)
	

	def addChild(self,c):
		self.children.append(c)

	def __str__(self):
		return "{1}  {0}".format(self.name,self.type)
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

class mapparser:

	def __init__(self,i):
		self.ast = Node('root') #root of the AST
		self.lexer.input(i)
		self.lexer = self.lexer.lex()
		self.parser=yacc(modules=self,write_tables=0,debug=False)

		while 1:
			tok = lex.token()
			if not tok: break
				#print tok

		yacc.yacc()
		yacc.parse(i,lexer=l,tracking=True)


def p_id(t):
	'identifier : ID'
	t[0] = Node(t[1],'id')

def p_listE(t):
	'parameter_list : '
	t[0] = Node('','param_list')

	def p_fd(self,t):
		'function_definition : FUNC identifier LPAREN parameter_list RPAREN LBR statement_list RBR'
		t[0] = Node(self,t[2],'funcdef',[t[4],t[7]])
		self.ast = t[0]

	def p_id(self,t):
		'identifier : ID'
		t[0] = Node(self,t[1])

	def p_listE(self,t):
		'parameter_list : '
		t[0] = Node()

	def p_plist(self,t):
		'parameter_list : type_declaration'
		t[0] = Node('','param_list',[t[1]])

	def p_plist2(self,t):
		'parameter_list : parameter_list COMMA type_declaration'
		t[0] = Node(self,t[2],'param_list',[t[1],t[3]])

	def p_typedec(self,t):
		'type_declaration : TYPE identifier'
		t[0] = Node(self,t[1],'typedec',[t[2]])

	def p_slist2(self,t):
		'statement_list : statement_list statement SEMICOLON'
		t[0] = Node('','statement_list',[t[1],t[2]])
		
	def p_slist(self,t):
		'statement_list : statement SEMICOLON'
		t[0] = Node('','statement_list',[t[1]])

	def p_slist3(self,t):
		'statement_list : '
		t[0] = Node()

	def p_s(self,t):
		'''statement : expression
		| function_call'''
		t[0] = Node('','statement',[t[1]])

	'''| selection-statement
	| iteration-statement'''

	#if statement
	def p_sels(self,t):
		'selection_statement : IF LPAREN expression RPAREN statement'
		t[0] = Node(self,t[1],'selection_statement',[t[3],t[5]])

	#else statement
	def p_sels2(self,t):
		'selection_statement : IF LPAREN expression RPAREN statement ELSE statement'
		t[0] = Node(self,t[1],'selection_statement',[t[3],t[5],t[7]])


	'''
	#for loop
	def p_iters(self,t):
		'iteration-statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement' #compound-statement?
		t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7] + t[8] + t[9]

	#foreach
	def p_ters2(self,t):
		'iteration-statement : FOREACH LPAREN identifier IN identifier RPAREN statement' #compound-statement
		t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7]'''

	#assignment
	def p_expr(self,t):
		'expression : assignment_expression'
		t[0] = Node('','expr',[t[1]])

	#Conditional expression
	def p_aexpr(self,t):
		'assignment_expression : conditional_expression'
		t[0] = Node('','assignment_expression',[t[1]])

	def p_aexpr2(self,t):
		'assignment_expression : primary_expression EQUALS assignment_expression'
		t[0] = Node(self,t[2],'assignment_expression',[t[1],t[3]])

	def p_condexpr(self,t):
		'''conditional_expression : logical_OR_expression
		| logical_AND_expression'''
		t[0] = Node('','conditional_expression',[t[1]])

	def p_logorexpr(self,t):
		'logical_OR_expression : logical_AND_expression'
		t[0] = Node('','logical_or_expr',[t[1]])

	def p_logorexpr2(self,t):	
		'logical_OR_expression : logical_OR_expression LOGICALOR logical_AND_expression'
		t[0] = Node(self,t[2],'',[t[1],t[3]])

	def p_logandexpr(self,t):
		'logical_AND_expression : equality_expression'
		t[0] = Node('','logical_and_expr',[t[1]])

	def p_logandexpr2(self,t):
		'logical_AND_expression : logical_AND_expression LOGICALAND equality_expression'
		t[0] = Node(self,t[2],'logical_and_expr',[t[1],t[3]])

	def p_eqexpr(self,t):
		'equality_expression : relational_expression'
		t[0] = Node('','equality_expression',[t[1]])

	def p_eqexpr2(self,t):
		'''equality_expression : equality_expression EQUALSEQUALS relational_expression
		| equality_expression DOESNOTEQUAL relational_expression'''
		t[0] = Node(self,t[2],'equality_expression',[t[1],t[3]])

	def p_relexpr(self,t):
		'relational_expression : additive_expression'
		t[0] = Node('','relational_expression',[t[1]])

	def p_relexpr2(self,t):
		'''relational_expression : relational_expression GREATERTHAN additive_expression
		| relational_expression LESSTHAN additive_expression
		| relational_expression LESSTHANOREQUALTO additive_expression
		| relational_expression GREATERTHANOREQUALTO additive_expression'''
		t[0] = Node(self,t[2],'relational_expression',[t[2],t[3]])

	def p_addexpr(self,t):
		'additive_expression : multiplicative_expression'
		t[0] = Node('','additive_expression',[t[1]])

	def p_addexpr2(self,t):
		'''additive_expression : additive_expression PLUS multiplicative_expression
		| additive_expression MINUS multiplicative_expression'''
		t[0] = Node(self,t[2],'additive_expression', [t[1],t[3]])

	def p_multexpr(self,t):
		'multiplicative_expression : primary_expression'
		t[0] = Node('','multiplicative_expression',[t[1]])

	def p_multexpr2(self,t):
		'''multiplicative_expression : multiplicative_expression TIMES primary_expression
		| multiplicative_expression DIVIDE primary_expression'''
		t[0] = Node(self,t[2],'multiplicative_expression',[t[1], t[3]])

	def p_primexp(self,t):
		'''primary_expression : identifier
		| type_declaration'''
		t[0] = Node('','primary_expression',[t[1]])

	def p_primexp_term(self,t):
		'''primary_expression : LITERAL
		| NUMERIC'''
		t[0] = Node('','primary_expression',[Node(self,t[1])])

	def p_primexp2(self,t):
		'''primary_expression : LPAREN expression RPAREN'''	
		t[0] = Node('','primary_expression', [t[2]])

	def p_funcall(self,t):
		'function_call : identifier PERIOD function_name LPAREN parameter_list RPAREN'
		t[0] = Node(self,t[2],'function_call',[t[1],t[3],t[5]])

	def p_funcall2(self,t):
		'function_call : identifier LPAREN func_args RPAREN'
		t[0] = Node('','function_call',[t[1], t[3]])

	def p_funcargs(self,t):
		'func_args : arg'
		t[0] = Node('','func_args',[t[1]])

	def p_funcargs2(self,t):
		'func_args : func_args COMMA arg'
		t[0] = Node(self,t[2],[t[1],t[3]])

	def p_arg_lit(self,t):
		'arg : LITERAL'
		t[0] = Node('','arg',[Node(self,t[1])])

	def p_arg_id(self,t):
		'arg : identifier'
		t[0] = Node('','arg',[t[1]])


	def p_arg_E(self,t):
		'arg : '
		t[0] = Node()

	def p_funcname(self,t):
		'''function_name : ADD
		| DELETEFUNC
		| ADJACENTFUNC
		| PATHFUNC
		| GETEDGEFUNC
		| ADDEDGEFUNC
		| DELETEEDGEFUNC
		| FINDSHORTESTFUNC
		| EQUALSFUNC'''
		t[0] = Node('','function_name',[t[1]])

	#i = "func main(self,Text hi, Text bye) { Numeric n = 1+2;}"
	#i = "func main(self,Text hi, Numeric bye) {print(hi);}"
	#i = "func main(self,Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2}"
	#i = "func main(self,Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore = 1; Text hello = 2; hello = oneMore + hello;}"

	def p_error(self,t):
		import inspect
		frame = inspect.currentframe()
		cvars = frame.f_back.f_locals
		#pprint (cvars)
		print "SYNTAX ERROR:"
		print 'Expected:', ', '.join(cvars['actions'][cvars['state']].keys())
		print 'Found:', cvars['ltype']
		print 'Errtoken: {0}'.format(cvars['errtoken'])
		print "input: {0}".format(i)



#while 1:
#	tok = lex.token()
#	if not tok: break
def p_slist2(t):
	'statement_list : statement_list statement SEMICOLON'
	t[0] = Node('','statement_list',[t[1],t[2]])
	
def p_slist(t):
	'statement_list : statement SEMICOLON'
	print "statement_list"
	t[0] = Node('','statement_list',[t[1]])

def p_slist3(t):
	'statement_list : '
	t[0] = Node('','statement_list_E')

def p_s(t):
	'''statement : expression
	| function_call'''
	print "statement"
	t[0] = Node('','statement',[t[1]])

'''| selection-statement
| iteration-statement'''

#if statement
def p_sels(t):
	'selection_statement : IF LPAREN expression RPAREN statement'
	t[0] = Node(t[1],'selection_statement',[t[3],t[5]])

#else statement
def p_sels2(t):
	'selection_statement : IF LPAREN expression RPAREN statement ELSE statement'
	t[0] = Node(t[1],'selection_statement',[t[3],t[5],t[7]])


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
	'expression : assignment_expression'
	print "expression"
	t[0] = Node('','expr',[t[1]])

#Conditional expression
def p_aexpr(t):
	'assignment_expression : conditional_expression'
	t[0] = Node('','assignment_expression',[t[1]])

def p_aexpr2(t):
	'assignment_expression : primary_expression EQUALS assignment_expression'
	t[0] = Node(t[2],'assignment_expression',[t[1],t[3]])

def p_condexpr(t):
	'''conditional_expression : logical_OR_expression
	| logical_AND_expression'''
	t[0] = Node('','conditional_expression',[t[1]])

def p_logorexpr(t):
	'logical_OR_expression : logical_AND_expression'
	t[0] = Node('','logical_or_expr',[t[1]])

def p_logorexpr2(t):	
	'logical_OR_expression : logical_OR_expression LOGICALOR logical_AND_expression'
	t[0] = Node(t[2],'',[t[1],t[3]])

def p_logandexpr(t):
	'logical_AND_expression : equality_expression'
	t[0] = Node('','logical_and_expr',[t[1]])

def p_logandexpr2(t):
	'logical_AND_expression : logical_AND_expression LOGICALAND equality_expression'
	t[0] = Node(t[2],'logical_and_expr',[t[1],t[3]])

def p_eqexpr(t):
	'equality_expression : relational_expression'
	t[0] = Node('','equality_expression',[t[1]])

def p_eqexpr2(t):
	'''equality_expression : equality_expression EQUALSEQUALS relational_expression
	| equality_expression DOESNOTEQUAL relational_expression'''
	t[0] = Node(t[2],'equality_expression',[t[1],t[3]])

def p_relexpr(t):
	'relational_expression : additive_expression'
	t[0] = Node('','relational_expression',[t[1]])

def p_relexpr2(t):
	'''relational_expression : relational_expression GREATERTHAN additive_expression
	| relational_expression LESSTHAN additive_expression
	| relational_expression LESSTHANOREQUALTO additive_expression
	| relational_expression GREATERTHANOREQUALTO additive_expression'''
	t[0] = Node(t[2],'relational_expression',[t[2],t[3]])

def p_addexpr(t):
	'additive_expression : multiplicative_expression'
	t[0] = Node('','additive_expression',[t[1]])

def p_addexpr2(t):
	'''additive_expression : additive_expression PLUS multiplicative_expression
	| additive_expression MINUS multiplicative_expression'''
	t[0] = Node(t[2],'additive_expression', [t[1],t[3]])

def p_multexpr(t):
	'multiplicative_expression : primary_expression'
	t[0] = Node('','multiplicative_expression',[t[1]])

def p_multexpr2(t):
	'''multiplicative_expression : multiplicative_expression TIMES primary_expression
	| multiplicative_expression DIVIDE primary_expression'''
	t[0] = Node(t[2],'multiplicative_expression',[t[1], t[3]])

def p_primexp(t):
	'''primary_expression : identifier
	| type_declaration'''
	t[0] = Node('','primary_expression',[t[1]])

def p_primexp_term(t):
	'''primary_expression : LITERAL
	| NUMERIC'''
	t[0] = Node('','primary_expression',[Node(t[1])])

def p_primexp2(t):
	'''primary_expression : LPAREN expression RPAREN'''	
	t[0] = Node('','primary_expression', [t[2]])

def p_funcall(t):
	'function_call : identifier PERIOD function_name LPAREN parameter_list RPAREN'
	t[0] = Node(t[2],'function_call',[t[1],t[3],t[5]])

def p_funcall2(t):
	'function_call : identifier LPAREN func_args RPAREN'
	t[0] = Node('','function_call',[t[1], t[3]])

def p_funcargs(t):
	'func_args : arg'
	t[0] = Node('','func_args',[t[1]])

def p_funcargs2(t):
	'func_args : func_args COMMA arg'
	t[0] = Node(t[2],[t[1],t[3]])

def p_arg_lit(t):
	'arg : LITERAL'
	t[0] = Node('','arg',[Node(t[1])])

def p_arg_id(t):
	'arg : identifier'
	t[0] = Node('','arg',[t[1]])


def p_arg_E(t):
	'arg : '
	t[0] = Node()

def p_funcname(t):
	'''function_name : ADD
	| DELETEFUNC
	| ADJACENTFUNC
	| PATHFUNC
	| GETEDGEFUNC
	| ADDEDGEFUNC
	| DELETEEDGEFUNC
	| FINDSHORTESTFUNC
	| EQUALSFUNC'''
	t[0] = Node('','function_name',[t[1]])

#i = "func main(Text hi){hi = 'hello';}"
#i = "func main(Text hi, Text bye) { Numeric n = 1+2;}"
#i = "func main(Text hi, Numeric bye) {print(hi);}"
#i = "func main(Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2}"
#i = "func main(Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore = 1; Text hello = 2; hello = oneMore + hello;}"

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

