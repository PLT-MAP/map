import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    check = True
    print(check)
    num = 5.0
    print(str(str(num) + str(" ")) + str(check))
    sentence = "Ima eat yo face"
    print(sentence)
    g = nx.MultiDiGraph()
    nj = 'nj',{}
    ny = 'ny',{}
    fl = 'fl',{}
    pa = 'pa',  {'temp':85.0,'humidity':'low'}
    va = 'va',  {'temp':87.0,'humidity':'high'}
    print(nj)
    print(pa)
    flight1=nj[0],ny[0],{}
    flight2=ny[0],pa[0],{}
    flight3=pa[0],va[0], {'cost':302.0,'distance':4092.0}
    flight4=va[0],nj[0],{}
    flight5=nj[0],fl[0], {'cost':50.0,'distance':5000.0}
    print(flight1)
    print(flight3)
    g.add_nodes_from([(nj[0], nj[1])])
    g.add_nodes_from([(ny[0], ny[1])])
    g.add_nodes_from([(fl[0], fl[1])])
    g.add_nodes_from([(pa[0], pa[1])])
    g.add_nodes_from([(va[0], va[1])])
    g.add_edges_from([(flight1[0],flight1[1],flight1[2])])
    g.add_edges_from([(flight2[0],flight2[1],flight2[2])])
    g.add_edges_from([(flight3[0],flight3[1],flight3[2])])
    g.add_edges_from([(flight4[0],flight4[1],flight4[2])])
    g.add_edges_from([(flight5[0],flight5[1],flight5[2])])
    print(g)
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'