import sys
import unittest
import yacc
import MAPlexer 



class TestYaccSyntax(unittest.TestCase):

	def setUp(self):
		self.lex=MAPlexer.MAPlex()

	def testhelloworld(self):
		test= "func main(Text hi, Numeric bye) { Text t = 'Hello, world'; bye = 2}"
		result=yacc.MAPparser(self.lex,test)
		print result

	def testprintfunc(self):
		test= "func main(Text hi, Numeric bye) {print('hi');}"
		result=yacc.MAPparser(self.lex,test)
		print result

	def testarithmetic(self):
		test=  "func main(Text hi, Text bye) { Numeric n = 1+2;}"
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunc(self):
		test = "func main(Text hi, Numeric hello, Path hereisApath, Node heresanode){ Text oneMore = 1; Text hello = 2; hello = oneMore + hello;}"
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunction(self):
		test='''
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
		result=yacc.MAPparser(self.lex,test)
		print result
	def testgraphfunction1(self):
		test='''
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
		result=yacc.MAPparser(self.lex,test)
		print result







if __name__ == "__main__": 
	unittest.main()
