#creating node types
#nodes are put into lists
#nodes with attributes will be stored in a dictionary in the first index
import networkx as nx
def main():	
	g=nx.MultiDiGraph()
	nj = ["nj"]
	ny = ["ny"]
	pa = ["pa", {'temp':85,'humidity':'low'}]
	va = ["va", {'temp':87,'humidity':'high'}]
	print g.nodes()
	
if __name__== '__main__':
	main()




