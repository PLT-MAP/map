import networkx as nx
import sys
def factorial(n):
    if (n==0.0):
        return 1.0
    x = 1.0
    for i in range(1, n+1):
        x = (x*i)
    return x
def main():
    fact = factorial(5.0)
    print fact
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'
