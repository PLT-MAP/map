#adding nodes to the graph
#nodes with no attributes will just have its 0th index added
#nodes with attributes will have its 0th and 1st index added
import networkx as nx
def main():
        g=nx.MultiDiGraph()
        nj = ["nj"]
        ny = ["ny"]
        pa = ["pa", {'temp':85,'humidity':'low'}]
        va = ["va", {'temp':87,'humidity':'high'}]
	#adding the nodes
	g.add_node(nj[0])
	g.add_node(ny[0])
	g.add_node(cookies)
	g.add_nodes_from([(pa[0],pa[1]),(va[0],va[1])])
	print g.nodes(data=True)
	
if __name__== '__main__':
	main()









