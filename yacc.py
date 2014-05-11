import sys
import ply.yacc as yacc
from node import *
#import warnings

#warnings.filterwarnings("ignore")
class MAPparser():

	def __init__(self,l,i,deb=1):
		self.ast = Node('root') #root of the AST
		self.lexer = l
		self.lexer.build()
		self.input = i
		self.tokens = l.tokens
		self.parser=yacc.yacc(module=self,debug=deb)
		self.parser.parse(i)
		self.errored = False

	def p_translation_unit(self,t):
		'''translation_unit : external_declaration
		| translation_unit external_declaration'''
		if len(t) == 2:
			t[0] = Node(t[0],'translation_unit',[t[1]])
		else:
			t[0] = Node(t[0],'translation_unit',[t[1],t[2]])
		self.ast = t[0]

	def p_external_declaration(self,t):
		'''external_declaration : function_definition'''
		t[0] = Node(t[0],'external_declaration',[t[1]])

	def p_fd(self,t):
		'function_definition : FUNC identifier LPAREN parameter_list RPAREN LBR statement_list RBR'
		t[0] = Node(t[2].name,'funcdef',[t[4],t[7]])

	def p_id(self,t):
		'identifier : ID'
		t[0] = Node(t[1],'id', t[1])

	def p_listE(self,t):
		'parameter_list : '
		t[0] = Node('','param_list')

	def p_plist(self,t):
		'parameter_list : type_declaration'
		t[0] = Node('','param_list',[t[1]])

	def p_plist2(self,t):
		'''parameter_list : parameter_list COMMA type_declaration
		| parameter_list COMMA parameter_list'''
		t[0] = Node(t[2],'param_list',[t[1],t[3]])

	# def p_plist3(self,t):
	# 	'parameter_list : associative_arr'

	def p_plist4(self, t):
		'''parameter_list : ID 
		| LITERAL '''
		t[0] = Node(t[1],'param_list',t[1])

	def p_typedec(self,t):
		'''type_declaration : TYPE identifier'''
		t[0] = Node(t[1],'typedec',[t[2]])

	def p_slist2(self,t):
		'statement_list : statement_list statement'
		t[0] = Node('','statement_list',[t[1],t[2]])

	def p_slist(self,t):
		'statement_list : statement'
		t[0] = Node('','statement_list',[t[1]])

	def p_slist3(self,t):
		'statement_list : '
		t[0] = Node('','statement_list')

	def p_s(self,t):
		'''statement : expression SEMICOLON
		| function_call SEMICOLON
		| selection_statement
		| for_loop
		| for_each
		| jump_stmt'''
		t[0] = Node('','statement',[t[1]])

	#if statement
	def p_sels(self,t):
		'selection_statement : IF LPAREN expression RPAREN LBR statement_list RBR sel_statement else_statement'
		t[0] = Node(t[1],'selection_statement',[t[3],t[6],t[8],t[9]])

	def p_sels2(self,t):
		'else_statement : ELSE LBR statement_list RBR'
		t[0] = Node(t[1],'else_statement',[t[3]])
	
	def p_sels3(self,t):
		'else_statement : '
		t[0] = Node('','else_statement')
	
	def p_sels4(self,t):
		'sel_statement : sel_statement elif_statement'
		t[0] = Node('','sel_statement',[t[1],t[2]])

	def p_sels5(self,t):
		'sel_statement : '
		t[0] = Node('','sel_statement')

	def p_sels6(self,t):
		'elif_statement : ELIF LPAREN expression RPAREN LBR statement_list RBR'
		t[0] = Node(t[1],'elif_statement',[t[3],t[6]])
	
	def p_sels7(self,t):
		'elif_statement : '
		t[0] = Node('','elif_statement')

	def p_for_loop(self,t):
		'''for_loop : FOR LPAREN aexpr SEMICOLON conditional_expression SEMICOLON assignment_expression RPAREN LBR statement_list RBR'''
		t[0] = Node(t[1],'for_loop',[t[3],t[5],t[7],t[10]])

	def p_for_each(self,t):
		'''for_each : FOREACH LPAREN TYPE identifier IN identifier RPAREN LBR statement_list RBR'''
		t[0] = Node(t[1],'for_each',[t[3],t[4],t[6],t[9]])

	def p_jump_stmt(self,t):
		'''
		jump_stmt : BREAK SEMICOLON
			  | CONTINUE SEMICOLON
			  | RETURN assignment_expression SEMICOLON
		'''
		if len(t) == 3:
			t[0]=Node(t[1], 'jump_stmt')
		else:
			t[0]=Node(t[1], 'jump_stmt', [t[2]])
		

	#assignment
	def p_expr(self,t):
		'''expression : assignment_expression
		| aexpr'''
		t[0] = Node('','expr',[t[1]])

	def p_aexpr5(self, t):
		''' aexpr : TYPE identifier EQUALS LITERAL
		| TYPE identifier EQUALS NUMERIC
		| TYPE identifier EQUALS BOOLEAN
		'''
 		t[0] = Node('aexpr','assignment_expression', [t[2],t[4]])

	def p_aexpr6(self, t):
		'''assignment_expression : TYPE identifier EQUALS function_call
		   | TYPE identifier EQUALS BOOLEAN'''
		t[0] = Node('equalsfunc','assignment_expression', [t[2],t[4]])

	#Conditional expression
	def p_aexpr(self,t):
		'''assignment_expression : conditional_expression
		| primary_expression
		| struct_assignment''' 
		t[0] = Node('','assignment_expression',[t[1]])

	def p_aexpr2(self,t):
		'''assignment_expression : primary_expression EQUALS assignment_expression'''
		t[0] = Node(t[2],'assignment_expression',[t[1],t[3]])

	def p_aexpr3(self,t):
		'''struct_assignment : TYPE identifier EQUALS NEW TYPE LPAREN func_args RPAREN'''
		t[0] = Node(t[2],'struct_assignment',[t[1],t[2],t[5],t[7]])

	def p_aexpr4(self,t):
		'''
		struct_assignment : TYPE identifier EQUALS NEW TYPE LPAREN RPAREN'''
		t[0] = Node(t[4],'struct_assignment',[t[1],t[2],t[5]])

	def p_condexpr(self,t):
		'''conditional_expression : logical_OR_expression
		| logical_AND_expression'''
		t[0] = Node('','conditional_expression',[t[1]])

	def p_logorexpr(self,t):
		'logical_OR_expression : logical_AND_expression'
		t[0] = Node('','logical_or_expr',[t[1]])

	def p_logorexpr2(self,t):
		'logical_OR_expression : logical_OR_expression LOGICALOR logical_AND_expression'
		t[0] = Node(t[2],'logical_or_expr',[t[1],t[3]])

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
		| multiplicative_expression DIVIDE primary_expression
		| multiplicative_expression MODULUS primary_expression'''
		t[0] = Node(t[2],'multiplicative_expression',[t[1], t[3]])

	def p_primexp(self,t):
		'''primary_expression : identifier
		| type_declaration'''
		t[0] = Node('','primary_expression',[t[1]])

	def p_primexp_term(self,t):
		'''primary_expression : LITERAL
		| NUMERIC'''
		t[0] = Node(t[1],'primary_expression',[Node(t[1],'primary_expression_ln')])

	def p_primexp2(self,t):
		'''primary_expression : LPAREN expression RPAREN'''
		t[0] = Node('','primary_expression', [t[2]])

	def p_funcall(self,t):
		'function_call : identifier PERIOD function_name LPAREN parameter_list RPAREN'
		t[0] = Node(t[2],'function_call',[t[1],t[3],t[5]])

	def p_funcall2(self,t):
		'''function_call : identifier LPAREN func_args RPAREN
				|  function LPAREN func_args RPAREN'''
		
		t[0] = Node(t[1],'function_call',[t[1], t[3]])
	
	def p_printfunc(self,t):
		'''function : PRINT 
			| INPUT
			| WRITE
			| READ'''
		t[0] = Node(t[1],t[1]) 
	

	def p_funcargs(self,t):
		'''func_args : arg
		| function_call'''
		t[0] = Node('','func_args',[t[1]])

	def p_funcargs2(self,t):
		'''func_args : func_args COMMA arg'''
		t[0] = Node(t[2],'func_args',[t[1],t[3]])

	def p_funcargs3(self,t):
		'''func_args : func_args PLUS arg'''
		t[0] = Node('print','func_args',[t[1],t[3]])

	def p_arg_lit(self,t):
		'''arg : LITERAL
		| NUMERIC'''
		t[0] = Node(t[1],'arg')
	
	def p_arg_assoc(self,t):
		'arg : associative_arr'
		t[0] = Node('','arg',[t[1]])	

	# def p_assoc_array(self, t):
	# 	'associative_arr : LITERAL COMMA LBR array_values RBR'
	# 	t[0] = Node(t[0], 'associative_arr', [t[4],t[1]])

	def p_assoc_array2(self, t):
		'associative_arr : LBR array_values RBR'
		t[0] = Node(t[0], 'associative_arr', [t[2]])

	def p_array_values1(self, t):
		'''array_values : arrayval
		'''
		t[0] = Node(t[0], 'array_values',[t[1]])

	def p_array_values(self, t):
		'''array_values : arrayval COMMA arrayval
		| array_values COMMA arrayval
		'''
		t[0] = Node(t[0], 'array_values',[t[1],t[3]])

	def p_arrayval(self, t):
		'arrayval : LITERAL COLON primary_expression'
		t[0] = Node(t[0], 'arrayval',[t[1],t[3]])

	# def p_value(self, t):
	# 	'''val : LITERAL
	# 	| NUMERIC'''	
	# 	t[0] = Node(t[0], 'arg')

	def p_arg_id(self,t):
		'arg : ID'
		t[0] = Node(t[1],'arg')


	def p_arg_E(self,t):
		'arg : '
		t[0] = Node('','arg')

	def p_funcname(self,t):
		'''function_name : ADD
		| DELETEFUNC
		| ADJACENTFUNC
		| PATHFUNC
		| GETEDGEFUNC
		| ADDEDGEFUNC
		| DELETEEDGEFUNC
		| FINDSHORTESTFUNC
		| DRAWFUNC
		| NONEIGHBORSFUNC
		| NODESWONEIHGHBORSFUNC
		| EQUALSFUNC'''
		t[0] = Node(t[1],'function_name',[t[1]])

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
		#print 'Errtoken: {0}'.format(cvars['errtoken'])
		#print "input: {0}".format(self.input)
		self.errored = True
		sys.exit()


def main(argv):
	pass

if __name__ == '__main__':
	main(sys.argv)
