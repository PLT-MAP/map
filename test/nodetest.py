import networkx as nx
import sys
import matplotlib.pyplot as plt
def main():
    g = nx.MultiDiGraph()
    no2 = 'no2',  {'temp':90.0,'weather':'cloudy with a chance'}
    g.add_nodes_from([(no2[0], no2[1])])
    g.remove_node(no2[0])
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'