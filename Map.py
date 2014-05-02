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
	
	
	
	#Bruteforce
	test=t.complete()
	test1=test.split("\n")
	#print test1
	
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
	print test2
	#main body of file
	outputfile=filename[0]+".py"
	output=open(outputfile,'w')
	content=content+test2
	
	mainstatement="if __name__ == '__main__': \n\tmain()"
	content=content+mainstatement
	output.write(content)



if __name__ == '__main__':
	main(sys.argv)











