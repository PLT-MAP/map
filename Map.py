import yacc 
import MAPlexer 
import traverse 
import sys
from asciitree import * 

def main(argv):
	inputfile=argv[1]
	filename=inputfile.split('.')
	parser=yacc.MAPparser
	lex=MAPlexer.MAPlex()
	f=open(argv[1],'r')
	test=f.read()
	m=parser(lex,test)
	t=traverse.Traverse(m.ast)

	outputfile=filename[0]+".py"
	output=open(outputfile,'w')
	content=t.complete()
	mainstatement="if __name__ == '__main__': \n\tmain()"
	content=content+mainstatement
	output.write(content)

if __name__ == '__main__':
	main(sys.argv)











