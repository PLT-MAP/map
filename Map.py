import yacc 
import MAPlexer 
import traverse 
import sys
from asciitree import * 
from nltk.tokenize import *
import re
#sudo pip install -U pyyaml nltk

symbol_table={}
symbol_table['def']=0
symbol_table['print']=0
symbol_table['=']=0
symbol_table[':']=0
symbol_table['for']=0
symbol_table['else']=0
symbol_table['if']=0
symbol_table['elif']=0
symbol_table['for']=0
symbol_table['range']=0
symbol_table['return']=0
symbol_table['each']=0


def main(argv):
	#parse and translate map file
	inputfile=argv[1]
	filename=inputfile.split('.')
	parser=yacc.MAPparser
	lex=MAPlexer.MAPlex()
	f=open(argv[1],'r')
	test=f.read()
	m=parser(lex,test)
	t=traverse.Traverse(m.ast)
	#write the file

	#add more to the header here if necessary
	header="import networkx as nx\nimport sys\n"
	content=header
	
	
	
	#Bruteforce
	test=t.complete()
	test1=test.split("\n")
	#print test1
	
	test2=indentb(test1)
	test3=errorcheck(test1)
	print test2
	#main body of file
	outputfile=filename[0]+".py"
	output=open(outputfile,'w')
	content=content+test2
	
	mainstatement="if __name__ == '__main__': \n\tmain()"
	content=content+mainstatement
	output.write(content)

def indentb(test1):		
	scope=0
	numtab=0
	temptab=0
	test2=""

	for line in test1:
	
		while line.startswith('\t'):
			temptab+=1
			line=line[1:]
		if not line:
			#print "hi"
			temptab=0
			continue
		if temptab<numtab:
			numtab=temptab
			scope=scope-1
		else:
			numtab=temptab
		
		i=0
		space=''
		while i<scope:
			#print scope
			space+="    "
			i+=1
		line=space+line
		#print line

		if line.endswith(':'):
			scope+=1
			numtab=temptab
			#print scope
		temptab=0
		test2+=line+'\n'
	return test2



def errorcheck(test1):
	scope=0
	pattern=re.compile(r'\:|\=|\'[A-Za-z ,!]*\'|\"[A-Za-z ,!]*\"|[A-Za-z,!]*')
	test1=['def main(hi, bye):']
	for line in test1:
		toklist= list(regexp_tokenize(line,pattern))
		toklist=filter(None,toklist)
		print toklist
		if not toklist:
			continue
		if toklist[0]=='def':
			#add function name to outer scope
			symbol_table[toklist[1]]=scope
			scope+=1
			for item in toklist:
				if item not in symbol_table:
					symbol_table[item]=scope
					print item
			print symbol_table
		else:
			for item in toklist:
				#check if a literal
				if (item.startswith('\"') && item.endswith('\"')) ||(item.startswith('\'') && item.endswith('\'')):
					continue
				






	return


if __name__ == '__main__':
	main(sys.argv)











