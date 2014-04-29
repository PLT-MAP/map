import networkx as nx
def main():
        g=nx.Graph()
        nj = "nj"
        ny = "ny"
        pa = "pa"
        padict= {'temp':85,'humidity':'low'}
        va = "va"
        vadict= {'temp':87,'humidity':'high'}
	g.add_node(nj)
	g.add_node(ny)
	g.add_nodes_from([pa,va])
	print g.nodes()
	
if __name__== '__main__':
	main()









