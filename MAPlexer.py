import ply.lex as lex
import ply.yacc as yacc

import sys

class MAPlexer:
	reserved ={ 'null':'NULL',
		'include':'INCLUDE',
		#	'true' : 'TRUE', 
		#	'false' : 'FALSE',
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
		
		}

	Boolean=['true','false']
	Type=['Node','Path','Graph','Text','Numeric']

	tokens = [
		'NUMERIC', 
		'TYPE',
		'BOOLEAN',
		#'SINGLEQUOTE', #2
		'DOUBLEQUOTE', 
		'ID',	   
		'PLUS',    
		'MINUS',   
		'TIMES',   
		'DIVIDE',  
		'LPAREN',  
		'RPAREN',  
		'MODULUS', 
		'SEMICOLON', 
		'COLON', 
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

	#converts string into float 
	def t_NUMERIC(self, t): 
		r'\d*\.?\d+'    #1
		t.value = str(float(t.value))
		return t

	#t_SINGLEQUOTE=r'(\')' #2
	t_DOUBLEQUOTE=r'(\")' #2.1

	def t_LITERAL(self, t):
		r'\'[A-Za-z ,!]*\''
		return t

	def t_ID(self, t): 
	 	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	 	t.type = self.reserved.get(t.value,'ID')
	 	if (t.value in self.Boolean):
			t.type='BOOLEAN'
		if (t.value in self.Type):
	 		t.type='TYPE'
			t.value= 'rue' in t.value  
	 	return t

	t_SEMICOLON = r';' 
	t_COLON = r'\:'
	t_PERIOD = r'\.'
	t_EXCLAMATION = r'\!'

	def t_FUNC(self, t):
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

	def t_error(self, t):
	    print "Illegal character '%s'" % t.value[0]
	    t.lexer.skip(1)
        
	def __init__(self,i):
        	self.lexer = lex.lex(module=self)
		self.lexer.input(i)

	def tokenize(self,data):
		'Debug method!'
		self.lexer.input(data)
		while True:
			tok = self.lexer.token()
			if tok:
				print tok
			else: 
				break
