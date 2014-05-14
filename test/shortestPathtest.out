import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    g = nx.MultiDiGraph()
    losangeles = 'losangeles',  {'temp':85.0,'humidity':'low'}
    boston = 'boston',  {'temp':87.0,'humidity':'high'}
    paris = 'paris',  {'temp':80.0}
    kansascity = 'kansascity',  {'temp':40.0,'humidity':'low'}
    sanfransisco = 'sanfransisco',  {'temp':30.0,'humidity':'low'}
    durham = 'durham',  {'temp':21.0,'humidity':'low'}
    minneapolis = 'minneapolis',  {'temp':41.0}
    stpaul = 'stpaul',  {'temp':50.0,'humidity':'low'}
    philly = 'philly',  {'temp':82.0,'humidity':'low'}
    pitts = 'pitts',  {'temp':90.0}
    stpeters = 'stpeters',  {'temp':100.0}
    g.add_nodes_from([(losangeles[0], losangeles[1])])
    g.add_nodes_from([(boston[0], boston[1])])
    g.add_nodes_from([(paris[0], paris[1])])
    g.add_nodes_from([(kansascity[0], kansascity[1])])
    g.add_nodes_from([(sanfransisco[0], sanfransisco[1])])
    g.add_nodes_from([(durham[0], durham[1])])
    g.add_nodes_from([(minneapolis[0], minneapolis[1])])
    g.add_nodes_from([(stpaul[0], stpaul[1])])
    g.add_nodes_from([(philly[0], philly[1])])
    g.add_nodes_from([(pitts[0], pitts[1])])
    g.add_nodes_from([(stpeters[0], stpeters[1])])
    laboston=losangeles[0],boston[0], {'cost':550.0}
    bostonparis=boston[0],paris[0], {'cost':100.0}
    parisla=losangeles[0],paris[0], {'cost':20.0}
    g.add_edges_from([(laboston[0],laboston[1],laboston[2])])
    g.add_edges_from([(bostonparis[0],bostonparis[1],bostonparis[2])])
    g.add_edges_from([(parisla[0],parisla[1],parisla[2])])
    try:
        nx.shortest_path(g,losangeles[0],paris[0],'cost')
    except:
        print 'no path'
    print g.get_edge_data(losangeles[0],paris[0])
    if (losangeles==losangeles):
        print("hi")
    else:
        print('bye')
    print "Graph:"
    print g
    print "Nodes:"
    print g.nodes(data=True)
    print "Node losangeles:"
    print losangeles
    print "Neighbors:"
    print g.neighbors(losangeles[0])
    print "shortest paths:"
    for nodeVal in g:
        try:
            print nx.shortest_path(g, source=losangeles[0], target=nodeVal[0])
        except:
            print "no path"
        print(nx.is_isolate(g,[0]))
        empty = nx.isolates(g)
        empty_nodes = nx.MultiDiGraph()
        print(empty)
        for x in empty:
            print(x)
            empty_nodes.add_nodes_from([(x[0], x[1])])
        nx.draw(empty_nodes)
        plt.show(empty_nodes)
        plt.savefig()
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'