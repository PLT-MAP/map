import networkx as nx
import matplotlib.pyplot as plt
def main():
        g=nx.MultiDiGraph()
        nj = "nj"
        ny = "ny"
        pa = "pa"
        padict= {'temp':85,'humidity':'low'}
        va = "va"
        vadict= {'temp':87,'humidity':'high'}
	flight1= ["nj","ny"]
	flight2 = ["ny", "pa"]
	flight3= ["pa","va"]
	flight3dict= {'cost':302, 'distance':4092}
        g.add_node(nj)
        g.add_node(ny)
        g.add_nodes_from([(pa,padict),(va,vadict)])
	g.add_edge(flight1[0],flight1[1])
	g.add_edges_from([(flight2[0],flight2[1])])
        print g.nodes(data=True)
	print g.edges()
	nx.draw(g)
	plt.show()

if __name__== '__main__':
        main()
