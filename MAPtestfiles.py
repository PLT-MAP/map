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
	Node va= new Node({'temp':87,'humidity':'high'});
}
'''
	sample2='''
	func main(){
	Graph g=new Graph();
	Node nj=new Node();
	Node ny=new Node();
	Node pa= new Node({'temp':85,'humidity':'low'});
	Node va= new Node({'temp':87,'humidity':'high'});
	g.add(nj);
	g.add(ny);
	g.add(pa);											
	}
	'''
	
	sample3='''
	func main(){
	Graph g=new Graph();
	Node nj=new Node();
	Node ny=new Node();
	Node fl=new Node();
	Node pa= new Node({'temp':85,'humidity':'low'});
	Node va= new Node({'temp':87,'humidity':'high'});
	DirEdge flight1= new DirEdge(nj, ny);
	DirEdge flight2= new DirEdge(ny, pa);
	DirEdge flight3= new DirEdge(pa, va, {'cost':302, 'distance':4092});
	UnDirEdge flight4= new UnDirEdge(va, nj);
	UnDirEdge flight5 = new UnDirEdge(nj,fl, {'cost':50, 'distance':5000});
	g.add(nj);	
	g.add(ny);
	g.add(fl);
	g.add(pa);
	g.add(va);
	g.addEdge(flight1);
	g.addEdge(flight2);
	g.addEdge(flight3);
	g.addEdge(flight4);
	g.addEdge(flight5);
	}
	'''

	sample4='''
	func main(){
		Boolean check = true;
		print (check);
		Numeric num = 5;
		print (num + " " + check);
		Text sentence= "Ima eat yo face";
		print (sentence);

		Graph g=new Graph();
		Node nj=new Node();
		Node ny=new Node();
		Node fl=new Node();
		Node pa= new Node({'temp':85,'humidity':'low'});
		Node va= new Node({'temp':87,'humidity':'high'});
		print (nj);
		print (pa);
		DirEdge flight1= new DirEdge(nj, ny);
		DirEdge flight2= new DirEdge(ny, pa);
		DirEdge flight3= new DirEdge(pa, va, {'cost':302, 'distance':4092});
		UnDirEdge flight4= new UnDirEdge(va, nj);
		UnDirEdge flight5 = new UnDirEdge(nj,fl, {'cost':50, 'distance':5000});
		print (flight1);
		print (flight3);
		g.add(nj);
		g.add(ny);
		g.add(fl);
		g.add(pa);
		g.add(va);
		g.addEdge(flight1);
		g.addEdge(flight2);
		g.addEdge(flight3);
		g.addEdge(flight4);
		g.addEdge(flight5);
		print(g);
	}
	'''

	sample5='''
	func main(){
	Graph g=new Graph();
	Node nj=new Node();
	Node ny=new Node();
	Node fl=new Node();
	Node pa= new Node({'temp':85,'humidity':'low'});
	Node va= new Node({'temp':87,'humidity':'high'});
	DirEdge flight1= new DirEdge(nj, ny);
	DirEdge flight2= new DirEdge(ny, pa);
	DirEdge flight3= new DirEdge(pa, va, {'cost':302, 'distance':4092});
	UnDirEdge flight4= new UnDirEdge(va, nj);
	UnDirEdge flight5 = new UnDirEdge(nj,fl, {'cost':50, 'distance':5000});
	g.add(nj);
	g.add(ny);
	g.add(fl);
	g.add(pa);
	g.add(va);
	g.addEdge(flight1);
	g.addEdge(flight2);
	g.addEdge(flight3);
	g.addEdge(flight4);
	g.addEdge(flight5);
	g.delete(pa);
	g.delete(va);
	g.delete(ny);
	g.deleteEdge(nj,ny);
}

	
	
	'''

	sample6='''
	func main(){
		Graph g=new Graph();
		Node nj=new Node();
		Node ny=new Node();
		Node fl=new Node();
		Node pa= new Node({'temp':85,'humidity':'low'});
		Node va= new Node({'temp':87,'humidity':'high'});
		DirEdge flight1= new DirEdge(nj, ny);
		DirEdge flight2= new DirEdge(ny, pa);
		DirEdge flight3= new DirEdge(pa, va, {'cost':302, 'distance':4092});
		UnDirEdge flight4= new UnDirEdge(va, nj);
		UnDirEdge flight5 = new UnDirEdge(nj,fl, {'cost':50, 'distance':5000});
		g.add(nj);
		g.add(ny);
		g.add(fl);
		g.add(pa);
		g.add(va);
		g.addEdge(flight1);
		g.addEdge(flight2);
		g.addEdge(flight3);
		g.addEdge(flight4);
		g.addEdge(flight5);
		Boolean check1= g.adjacent(nj, pa);
		print (check1);
		Boolean check2= g.adjacent(nj, ny);
		print (check2); 
		Path p1 = g.path(nj);
		Path p2 = g.path(pa);
		if (p1 == p2){
			print("yo");
		}

	}
	'''

	pathtest='''
		func main(){
		Path p = new Path(g);
		p.add(nj);
  	}
	'''

	def __init__(self):
		pass
