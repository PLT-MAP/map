import yacc 
import MAPlexer 
import traverse 
import sys

def main(argv):
	inputfile=argv[1]
	print inputfile

	filename=inputfile.split('.')
	print filename[0]
	print filename[1]
	parser=yacc.MAPparser


if __name__ == '__main__':
	main(sys.argv)











