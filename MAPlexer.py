import ply.lex as lex

tokens = (
	
	'NUMERIC',
	'DECIMAL',
	'TEXT',
	'BOOLEAN',
	'TIME',
	
	'NULL',
	'EDGE',
	'NODE',
	'PATH',
	
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LPAREN',
	'RPAREN',
	
	'LESSTHAN',
	'GREATERTHAN',
	'LESSTHANOREQUALTO',
	'GREATERTHANOREQUALTO',
	'EQUALSEQUALS',
	'DOESNOTEQUAL',
	
	'AMPERSAN',
	'LOGICALAND',
	'LOGICALOR',
	
	'COMMENT',
	'COMMENTFRONT',
	'COMMENTBACK'
	)

t_NUMERIC=r'(\d+)'
t_DECIMAL=r'\d + \.+\d+'

t_LOGICALOR=r'\|'
t_LOGICALAND=r'&'




def t_BOOLEAN(t):
	r'(True | False | true | false)'
	t.value='rue' in t.value
	return t

t_NULL=r'NULL'
t_COMMENT=r'//'
t_COMMENTBACK=r'(\*/)'
t_COMMENTFRONT=r'(/\*)'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LESSTHAN=r'\<'
t_GREATERTHAN=r'\>'
t_LESSTHANOREQUALTO=r'<\='
t_GREATERTHANOREQUALTO=r'>\='
t_EQUALSEQUALS=r'=='
t_DOESNOTEQUAL=r'!='

t_ignore  = ' \t'
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)



test='1000000.00000'
lexer=lex.lex()
lexer.input(test)

print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()
print lexer.token()

