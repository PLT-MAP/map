import ply.lex as lex
#http://flex.sourceforge.net/manual/Patterns.html
reserved ={ 'null':'NULL',
	'include':'INCLUDE',
	'true' : 'TRUE', 
	'false' : 'FALSE',
	'Time':'TIME',
	'DirEdge':'DIREDGE',
	'UndirEdge':'UNDIREDGE',
	'Print':'PRINT', 
	'add':'ADD',
	'Delete':'DELETEFUNC',
	'path':'PATHFUNC',
	'adjacent':'ADJACENTFUNC',
	'getEdge':'GETEDGEFUNC',
	'addEdge':'ADDEDGEFUNC',
	'deleteEdge':'DELETEEDGEFUNC',
	'findShortest':'FINDSHORTESTFUNC',
	'equals':'EQUALSFUNC',
	'in':'IN',
	'if':'IF', 
	'for':'FOR', 
	'break':'BREAK', 
	'elif':'ELIF', 
	'foreach':'FOREACH',
	'continue':'CONTINUE',
	'return':'RETURN',
	'else':'ELSE', 
	'read':'READ', 
	'write':'WRITE',
	'func':'FUNC',
	'Node':'TYPE',
	'Path':'TYPE',
	'Graph':'TYPE',
	'Text':'TYPE',
	'Numeric':'TYPE'
}

tokens = [
	'NUMERIC', #1
	#'SINGLEQUOTE', #2
	'DOUBLEQUOTE', #2.1
	'ID',	   #3
	'PLUS',    #11
	'MINUS',   #12
	'TIMES',   #13
	'DIVIDE',  #14
	'LPAREN',  #15
	'RPAREN',  #16
	'MODULUS', #16.1
	'SEMICOLON', # 16.2
	'COLON', # 16.3
	'LESSTHAN', #17
	'GREATERTHAN', #18
	'EQUALS', 
	'LESSTHANOREQUALTO', #19
	'GREATERTHANOREQUALTO', #20
	'EQUALSEQUALS', #21
	'DOESNOTEQUAL', #22	
	'LOGICALAND', #24
	'LOGICALOR',  #25
	'LOGICALNOT',
	'COMMENT',    #26
	'COMMENTFRONT', #27
	'COMMENTBACK',   #28
	'COMMA', #37
	'NEWLINE',#38
	'LBR', # 40
	'RBR', # 41
	'LSB', 
	'RSB',
	'PERIOD',
	'EXCLAMATION',
	'LITERAL',
	]+list(reserved.values())
'''
def t_TYPE(t):
	r'^Text$|^Numeric$'
	return t
'''
#primitive data types

#converts string into float 
def t_NUMERIC(t): 
	r'\d*\.?\d+'    #1
	t.value = float(t.value)
	return t

#t_SINGLEQUOTE=r'(\')' #2
t_DOUBLEQUOTE=r'(\")' #2.1

def t_LITERAL(t):
	r'\'[A-Za-z ,!]*\''
	return t

def t_ID(t): 
 	r'[a-zA-Z_][a-zA-Z_0-9]*' 
 	t.type = reserved.get(t.value,'ID')
 	return t

t_SEMICOLON = r';' 
t_COLON = r'\:'
t_PERIOD = r'\.'
t_EXCLAMATION = r'\!'

def t_FUNC(t):
	r'^func\s'
	return t 

#def t_BOOLEAN(t): #4
#	r'(True | False | true | false)'
#	t.value= 'rue' in t.value
#	return t

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
t_EQUALS = r'\='
t_EQUALSEQUALS=r'\=\='#21
t_DOESNOTEQUAL=r'!='#22
t_LOGICALAND=r'&'  #24
t_LOGICALOR=r'\|'  #25
t_LOGICALNOT=r'!' 

#commenting
t_COMMENT=r'//' #26
t_COMMENTBACK=r'(\*/)' #27
t_COMMENTFRONT=r'(/\*)'#28
t_LSB = '\['
t_RSB = '\]'
t_LBR = '\{'
t_RBR = '\}'


t_COMMA=r'\,' #37

t_NEWLINE=r'\n'#38

t_ignore  = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


lexer=lex.lex()

#lex.input("func main(hi, bye) { Text t = 'Hello, world'; print(t);}")

#lex.input("func main(Text hi, Numeric bye) { Text t = 'Hello, world'; print(t);}")

#while 1:
#	tok = lex.token()
#	if not tok: break
#	print tok
