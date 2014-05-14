import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    g = nx.MultiDiGraph()
    losangeles = 'losangeles',  {'temp':90.0,'humidity':'low'}
    sanjose = 'sanjose',  {'temp':50.0,'humidity':'low'}
    sanfransisco = 'sanfransisco',  {'temp':65.0,'humidity':'high'}
    paris = 'paris',  {'temp':30.0,'weather':'snowing'}
    g.add_nodes_from([(losangeles[0], losangeles[1])])
    g.add_nodes_from([(sanjose[0], sanjose[1])])
    g.add_nodes_from([(sanfransisco[0], sanfransisco[1])])
    g.add_nodes_from([(paris[0], paris[1])])
    la_sj=losangeles[0],sanjose[0], {'cost':100.0}
    sj_sf=sanjose[0],sanfransisco[0], {'cost':50.0}
    la_sf=losangeles[0],sanfransisco[0], {'cost':180.0}
    g.add_edges_from([(la_sj[0],la_sj[1],la_sj[2])])
    g.add_edges_from([(sj_sf[0],sj_sf[1],sj_sf[2])])
    g.add_edges_from([(la_sf[0],la_sf[1],la_sf[2])])
    print g.get_edge_data(losangeles[0],sanfransisco[0])
    print("Shortest path between Los Angeles and San Fransisco: ")
    try:
        print nx.shortest_path(g,losangeles[0],sanfransisco[0],'cost')
        print nx.shortest_path_length(g,losangeles[0],sanfransisco[0], 'cost')
    except:
        print 'no path'
    print("Unconnected nodes in graph g: ")
    print(nx.isolates(g))
    pos = nx.spring_layout(g)
    nx.draw(g, pos)
    node_labels = nx.get_node_attributes(g,'cost')
    nx.draw_networkx_labels(g, pos, labels = node_labels)
    edge_labels = nx.get_edge_attributes(g,'cost')
    nx.draw_networkx_edge_labels(g, pos, labels = edge_labels)
    plt.show(g)
    plt.savefig("shortest.jpeg")
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'