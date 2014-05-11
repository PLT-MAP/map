class MapTests(object):

	helloworld="""
	func main() {  
	Text t = 'Hello, world';   
	Numeric bye = 2;
	print(t);
}
	"""
	print_statement="""
	func main(){
		print('hi');
	}
	"""



	iftest=""" 
	func main(){
	if (5 < 7) {
		cost = 5;
		}
	}
	"""

	ifelsetest="""
	func main() {                                                                     
		if (10<7){ 
			cost= 2;                                               
			}                                                                    
		else{  
				print("success");  
			}                 
		}
	"""

	ifelifelsetest="""
	func main(){
	if(x<5){
		cost=5;
	}
	elif (x<10)
	{
		cost=10;
	}
	else{
		cost=15;
	}
	}
	"""

	for_statement="""
func main(){
	for(Numeric i=0;i<10;i=i+2){
	print(i);
	}
}
	"""

	foreach_statement="""
	func main(){
		foreach (Node n in graph){
		print(n);
		}
	}
	"""

	nodetest="""
	func main(){
        Graph g = new Graph();
        Node no2 = new Node( {'temp':90, 'weather': 'cloudy with a chance'});
        g.add(no2);
        g.delete(no2);

	}
	"""
	graph='''
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

		func main(){
		createTrip();
		}
		'''
	graphfile='''
		func printDestination(Node origin, Graph graph) {       
		Numeric min= 100000;
		Edge temp;
		Edge minEdge;
		foreach (Node n in graph) {
			if (n['humidity'] == 'low' && graph.adjacent(origin, n)) {
				temp = graph.getEdge(origin, n);
				if (temp['cost'] < min) {
					min = temp['cost'];
					minEdge = temp;
				}
			}
		}
		print(minEdge);
		}

		func main() {
		Graph trip = createTrip();
		printDestination(seattle, trip);
		}
		'''

	rwtest = '''func main(){
		Graph g = new Graph();
		Node no2 = new Node( {'temp':90, 'weather': 'cloudy with a chance'});
		g.add(no2);
		Text filepath = "someFilename";
		write(filepath,g);
		Graph g2 = read(filepath);
	}'''
	

	sample1='''
	func main(){
        Graph g=new Graph();
        Node nj= new Node();
        Node ny= new Node();
        Node pa= new Node({'temp':85,'humidity':'low'});
		Node va= new Node({'temp':87,'humidity':'high'});}
	'''
	pathtest='''
		func main(){
		Path p = new Path(g);
		p.add(nj);
  	}
	'''

	def __init__(self):
		pass
