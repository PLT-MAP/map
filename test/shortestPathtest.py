import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    g = nx.MultiDiGraph()
    losangeles = 'losangeles',  {'temp':90.0,'humidity':'low'}
    sanjose = 'sanjose',  {'temp':50.0,'humidity':'low'}
    sanfransisco = 'sanfransisco',  {'temp':65.0,'humidity':'high'}
    g.add_nodes_from([(losangeles[0], losangeles[1])])
    g.add_nodes_from([(sanjose[0], sanjose[1])])
    g.add_nodes_from([(sanfransisco[0], sanfransisco[1])])
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
    nx.draw(g)
    plt.show(g)
    plt.savefig("shortest.jpeg")
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'