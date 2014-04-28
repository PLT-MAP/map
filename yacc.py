import ply.yacc as yacc
from node import *

class MAPparser():

	def __init__(self,l,i):
		self.ast = Node('root') #root of the AST
		self.lexer = l
		self.lexer.build()
		self.input = i
		self.tokens = l.tokens
		self.parser=yacc.yacc(module=self)
		self.parser.parse(i)

	def p_fd(self,t):
		'function_definition : FUNC identifier LPAREN parameter_list RPAREN LBR statement_list RBR'
		t[0] = Node(t[2].name,'funcdef',[t[4],t[7]])
		self.ast = t[0]


	def p_id(self,t):
		'identifier : ID'
		t[0] = Node(t[1],'id')

	def p_listE(self,t):
		'parameter_list : '
		t[0] = Node('','param_list')

	def p_plist(self,t):
		'parameter_list : type_declaration'
		t[0] = Node('','param_list',[t[1]])

	def p_plist2(self,t):
		'parameter_list : parameter_list COMMA type_declaration'
		t[0] = Node(t[2],'param_list',[t[1],t[3]])

	def p_typedec(self,t):
		'type_declaration : TYPE identifier'
		t[0] = Node(t[1],'typedec',[t[2]])

	def p_slist2(self,t):
		'statement_list : statement_list statement'
		t[0] = Node('','statement_list',[t[1],t[2]])

	def p_slist(self,t):
		'statement_list : statement'
		t[0] = Node('','statement_list',[t[1]])

	def p_slist3(self,t):
		'statement_list : '
		t[0] = Node()

	def p_s(self,t):
		'''statement : expression SEMICOLON
		| function_call SEMICOLON
		| selection_statement'''
		t[0] = Node('','statement',[t[1]])

	#if statement
	def p_sels(self,t):
		'selection_statement : IF LPAREN expression RPAREN LBR statement_list RBR'
		t[0] = Node(t[1],'selection_statement',[t[3],t[6]])

	#else statement
	def p_sels2(self,t):
		'selection_statement : IF LPAREN expression RPAREN LBR statement_list RBR ELSE statement'
		t[0] = Node(t[1],'selection_statement',[t[3],t[6],t[9]])

	#assignment
	def p_expr(self,t):
		'expression : assignment_expression'
		t[0] = Node('','expr',[t[1]])

	#Conditional expression
	def p_aexpr(self,t):
		'''assignment_expression : conditional_expression
		| primary_expression''' 
		t[0] = Node('','assignment_expression',[t[1]])

	def p_aexpr2(self,t):
		'''assignment_expression : primary_expression EQUALS assignment_expression'''
		t[0] = Node(t[2],'assignment_expression',[t[1],t[3]])

	def p_condexpr(self,t):
		'''conditional_expression : logical_OR_expression
		| logical_AND_expression'''
		t[0] = Node('','conditional_expression',[t[1]])

	def p_logorexpr(self,t):
		'logical_OR_expression : logical_AND_expression'
		t[0] = Node('','logical_or_expr',[t[1]])

	def p_logorexpr2(self,t):
		'logical_OR_expression : logical_OR_expression LOGICALOR logical_AND_expression'
		t[0] = Node(t[2],'',[t[1],t[3]])

	def p_logandexpr(self,t):
		'logical_AND_expression : equality_expression'
		t[0] = Node('','logical_and_expr',[t[1]])

	def p_logandexpr2(self,t):
		'logical_AND_expression : logical_AND_expression LOGICALAND equality_expression'
		t[0] = Node(t[2],'logical_and_expr',[t[1],t[3]])

	def p_eqexpr(self,t):
		'equality_expression : relational_expression'
		t[0] = Node('','equality_expression',[t[1]])

	def p_eqexpr2(self,t):
		'''equality_expression : equality_expression EQUALSEQUALS relational_expression
		| equality_expression DOESNOTEQUAL relational_expression'''
		t[0] = Node(t[2],'equality_expression',[t[1],t[3]])

	def p_relexpr(self,t):
		'relational_expression : additive_expression'
		t[0] = Node('','relational_expression',[t[1]])

	def p_relexpr2(self,t):
		'''relational_expression : relational_expression GREATERTHAN additive_expression
		| relational_expression LESSTHAN additive_expression
		| relational_expression LESSTHANOREQUALTO additive_expression
		| relational_expression GREATERTHANOREQUALTO additive_expression'''
		t[0] = Node(t[2],'relational_expression',[t[1],t[3]])

	def p_addexpr(self,t):
		'additive_expression : multiplicative_expression'
		t[0] = Node('','additive_expression',[t[1]])

	def p_addexpr2(self,t):
		'''additive_expression : additive_expression PLUS multiplicative_expression
		| additive_expression MINUS multiplicative_expression'''
		t[0] = Node(t[2],'additive_expression', [t[1],t[3]])

	def p_multexpr(self,t):
		'multiplicative_expression : primary_expression'
		t[0] = Node('','multiplicative_expression',[t[1]])

	def p_multexpr2(self,t):
		'''multiplicative_expression : multiplicative_expression TIMES primary_expression
		| multiplicative_expression DIVIDE primary_expression'''
		t[0] = Node(t[2],'multiplicative_expression',[t[1], t[3]])

	def p_primexp(self,t):
		'''primary_expression : identifier
		| type_declaration'''
		t[0] = Node('','primary_expression',[t[1]])

	def p_primexp_term(self,t):
		'''primary_expression : LITERAL
		| NUMERIC'''
		t[0] = Node(t[1],'primary_expression',[Node(t[1])])

	def p_primexp2(self,t):
		'''primary_expression : LPAREN expression RPAREN'''
		t[0] = Node('','primary_expression', [t[2]])

	def p_funcall(self,t):
		'function_call : identifier PERIOD function_name LPAREN parameter_list RPAREN'
		t[0] = Node(t[2],'function_call',[t[1],t[3],t[5]])

	def p_funcall2(self,t):
		'function_call : identifier LPAREN func_args RPAREN'
		t[0] = Node('','function_call',[t[1], t[3]])

	def p_funcargs(self,t):
		'func_args : arg'
		t[0] = Node('','func_args',[t[1]])

	def p_funcargs2(self,t):
		'func_args : func_args COMMA arg'
		t[0] = Node(t[2],[t[1],t[3]])

	def p_arg_lit(self,t):
		'arg : LITERAL'
		t[0] = Node('','arg',[Node(t[1])])

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
		print "input: {0}".format(self.input)


def main(argv):
	pass

if __name__ == '__main__':
	main(sys.argv)
