import yacc 
import MAPlexer 
import traverse 
import sys
from preprocess import *

def main(argv):
	inputfile=argv[1]
	print inputfile

	filename=inputfile.split('.')
	print filename[0]
	print filename[1]
	
	parser=yacc.MAPparser
	lex=MAPlexer.MAPlex()


if __name__ == '__main__':
	main(sys.argv)











