import networkx as nx
import sys
def test():
    string = raw_input("Enter a string")
    return string
def main():
    test()
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'