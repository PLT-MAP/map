import networkx as nx
import sys
def main():
    g = nx.MultiDiGraph()
    nj = 'nj',{}
    ny = 'ny',{}
    pa = 'pa',  {'temp':85.0,'humidity':'low'}
    va = 'va',  {'temp':87.0,'humidity':'high'}
    g.add_nodes_from([(nj[0], nj[1])])
    g.add_nodes_from([(ny[0], ny[1])])

if __name__ == '__main__': 
	main()
