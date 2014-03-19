import ply.lex as lex
#http://flex.sourceforge.net/manual/Patterns.html
tokens = (
	
	'NUMERIC', #1
	'DECIMAL', #2
	'TEXT',	   #3
	'BOOLEAN', #4
	'TIME',    #5
	
	'NULL',    #6
	'EDGE',    #7
	'NODE',    #8
	'PATH',    #9
	'GRAPH',   #10
	
	'PLUS',    #11
	'MINUS',   #12
	'TIMES',   #13
	'DIVIDE',  #14
	'LPAREN',  #15
	'RPAREN',  #16
	
	'LESSTHAN', #17
	'GREATERTHAN', #18
	'LESSTHANOREQUALTO', #19
	'GREATERTHANOREQUALTO', #20
	'EQUALSEQUALS', #21
	'DOESNOTEQUAL', #22
	
	'AMPERSAN', #23
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
	'NEWLINE'#38





	)

#primitive data types
t_NUMERIC=r'(\d+)'   #1
t_DECIMAL=r'\d + \.+\d+' #2
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

def t_EDGE(t):
	r'Edge' 
	return t #7


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
t_AMPERSAN=r'\@'#23
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

t_GADD=r'\.add'          #30
t_GDELETE=r'\.delete'       #31
t_GADJACENT=r'\.adjacent'     #32
t_GPATH=r'\.path'         #33
t_GGETEDGE=r'\.getEdge'      #34
t_GADDEDGE=r'\.addEdge'      #35
t_GDELETEEDGE=r'\.deleteEdge'   #35
t_GFINDSHORTESTPATH=r'\.findShortestPath'   #36

t_COMMA=r'\,' #37
t_NEWLINE=r'\n'

t_ignore  = ' \t'
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)



test='Graph.addEdge(Node) disj dij \n'
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

