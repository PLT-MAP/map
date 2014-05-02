import yacc 
import MAPlexer 
import traverse 
import sys
from asciitree import * 

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
	header="import networkx\nimport sys\n"
	content=header
	
	#main body of file
	outputfile=filename[0]+".py"
	output=open(outputfile,'w')
	content=content+t.complete()

	mainstatement="if __name__ == '__main__': \n\tmain()"
	content=content+mainstatement
	output.write(content)

if __name__ == '__main__':
	main(sys.argv)











