import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    p = nx.MultiDiGraph()
    p.add_nodes_from([(nj[0], nj[1])])
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'