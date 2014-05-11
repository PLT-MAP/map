import networkx as nx
import sys
def main():
    g = nx.MultiDiGraph()
    no3 = 'no3',{}
    no2 = 'no2',  {'temp':90.0,'weather':'cloudy with a chance'}
    g.add_nodes_from([(no3[0], no3[1])])
    g.add_nodes_from([(no2[0], no2[1])])
    e=no2[0],no3[0], {'cost':100.0}
    g.add_edges_from([(e[0],e[1],e[2])])
    try:
        nx.shortest_path(g,no2[0],no3[0],'cost')
    except:
        print 'no path'
    print(g.get_edge_data(no2[0],no3[0]))
    p = nx.MultiDiGraph()
    print(p)
    p.add_nodes_from([(no3[0], no3[1])])
    p.add_nodes_from([(no2[0], no2[1])])
    if (no2==no3):
        print("hi")
    else:
        print('bye')
    print "Graph:"
    print g
    print "Nodes:"
    print g.nodes(data=True)
    print "Path:"
    print p
    print "Nodes:"
    print p.nodes(data=True)
    print "Node no2:"
    print no2
    print "Neighbors:"
    print g.neighbors(no2[0])
    print "shortest paths:"
    for nodeVal in g:
        try:
            print nx.shortest_path(g, source=no2[0], target=nodeVal[0])
        except:
            print "no path"
        print(nx.is_isolate(g,no2[0]))
        empty = nx.isolates(g)
        for lol in empty:
            print(n)
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'