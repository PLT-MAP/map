import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node(1)
G.add_node("e")
dict= {'cabo':,'cost':30}
G.add_node( dict)
G.add_edge(1,"e")
G.add_edge("e", "cabo")
print G.number_of_nodes()
print G.nodes(data=True)
print G.edges()
nx.draw(G)
plt.show()
