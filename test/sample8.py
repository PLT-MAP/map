import networkx as nx
import sys
def createItinerary():
    trip = nx.MultiDiGraph()
    seattleAirport = 'seattleAirport',  {'temp':85.0,'humidity':'low'}
    nyAirport = 'nyAirport',  {'temp':80.0,'humidity':'high'}
    flight5=seattleAirport[0],nyAirport[0], {'cost':302.0,'distance':4092.0}
    trip.add_nodes_from([(seattleAirport[0], seattleAirport[1])])
    trip.add_nodes_from([(nyAirport[0], nyAirport[1])])
    trip.add_edges_from([(flight5[0],flight5[1],flight5[2])])
    return trip
def main():
    trip = createItinerary()
    print "Graph:"
    print trip
    print "Nodes:"
    print trip.nodes(data=True)
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'