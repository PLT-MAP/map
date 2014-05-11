import networkx as nx
import sys
def main():
    x = 2.0
    if (x<5.0 and x>10.0):
        print("success")
    elif (x<10.0 or x>20.0):
        cost = 10.0
    else:
        cost = 15.0
    print(str("cost = ") + str(cost))
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'