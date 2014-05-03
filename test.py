import networkx as nx
def main():
	n = 'hi world'
	print n
	g = nx.MultiDiGraph()
	no2 = 'lol', {'temp':45.0,'cost':300.0,'weight':200.0,'weather':'cloudy with a chance'}
	g.add_node(no2[0], no2[1])
	g.remove_node(no2[0])
	print "got here"

main()

'''
		func createTrip() {
		Node cabo = Node({'temp':85,'humidity':'low'});
		Node miami = Node({'temp':87,'humidity':'high'});
		Node ontario = Node({'temp':45});
		Node seattle = Node({'temp':60,'humidity':'low'});
		Node sanfran = Node({'temp':75,'humidity':'low'});
		Node newyork = Node({'temp':50,'humidity':'medium'});
		Node la = Node({'temp':78});
		Graph flights = Graph(1);		// create directed graph
		flights.add(cabo, miami, ontario, seattle, sanfran, newyork, la);
		Edge flight5 = Edge(newyork, seattle, {'cost':330,'distance':4092,'duration':6.5,'date':2014.03.14.6.25});
		Edge flight9 = Edge(newyork, la, {'cost':256,'duration':6});
		Edge flight7 = Edge(la, cabo, {'cost':180','duration':2.5});
		Edge flight234 = Edge(newyork, sanfran, {'cost': 280,'duration': 6});
		Edge flight49 = Edge(seattle, cabo, {'cost':350,'duration':4.5});
		flights.addEdge(flight5, flight9, flight7, flight234, flight49);
		return flights;}
'''
