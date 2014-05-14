import networkx as nx
import sys
def main():
    g = nx.MultiDiGraph()
    g2 = nx.MultiDiGraph()
    g2 = g
    nj = 'nj',{}
    ny = 'ny',{}
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
    g.add_nodes_from([(paris[0], paris[1])])
    g.add_nodes_from([(durham[0], durham[1])])
    g.add_nodes_from([(philly[0], philly[1])])
    g.add_nodes_from([(pitts[0], pitts[1])])
    g.add_nodes_from([(stpeters[0], stpeters[1])])
    wee=nj[0],ny[0],{}
    lol=boston[0],paris[0],{}
    nynj=ny[0],nj[0], {'distance':100.0}
    pittsphilly=pitts[0],philly[0], {'distance':10.0}
    pittsparis=pitts[0],paris[0], {'distance':15.0}
    stpaulpitts=stpaul[0],pitts[0], {'distance':40.0}
    g.add_edges_from([(wee[0],wee[1],wee[2])])
    g.add_edges_from([(pittsphilly[0],pittsphilly[1],pittsphilly[2])])
    g.add_edges_from([(stpaulpitts[0],stpaulpitts[1],stpaulpitts[2])])
    g.add_edges_from([(pittsparis[0],pittsparis[1],pittsparis[2])])
    print(losangeles)
    g.has_edge(losangeles[0],paris[0])
    g.neighbors(losangeles[0])
    nx.draw(g)
    plt.show(g)
    plt.savefig()
    print "Graph:"
    print g
    print "Nodes:"
    print g.nodes(data=True)
    lol = (g.nodes() == .nodes() and g.edges() == .edges())
    print(lol)
    print g.get_edge_data(pitts[0],philly[0])
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'