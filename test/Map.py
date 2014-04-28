#import yacc 
#import MAPlexer 
#import traverse 
import sys

def main(argv):
	inputfile=argv[1]
	filename=inputfile.split('.')[0]
	print filename[0]
	print filename[1]

if __name__ == '__main__':
	main(sys.argv)











