import networkx as nx
import sys
def main():
    g = nx.MultiDiGraph()
    no2 = 'no2',  {'temp':90.0,'weather':'cloudy with a chance'}
    g.add_nodes_from([(no2[0], no2[1])])
    filepath = "someFilename"
    pickle.dump(g,open(filepath,"wb"))
    g2 = pickle.load(open(filepath,"rb"))
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'