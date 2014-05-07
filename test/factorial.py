import networkx as nx
import sys
def factorial(n):
    x = 1.0
    if (n==0.0):
        print(n)
    p = 10.0
    for i in range(1, int(p+1)):
        x = (x%i)
        return x>0.0
def main():
    fact = factorial(5.0)
    print("Reached here")
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'