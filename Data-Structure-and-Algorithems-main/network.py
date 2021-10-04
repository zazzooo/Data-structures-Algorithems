import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(range(1,10))
G.add_edge(1, 2, weight = 3)
G.add_edge(4, 2, weight = 2.4)
G.add_edge(6, 2,weight = 5)
G.add_edge(1, 8, weight = 6)
G.add_edge(3, 6,weight = 1)
G.add_edge(2, 7, weight = 2)
G.add_edge(9, 7, weight = 2)
G.add_edge(10, 7, weight = 2)
G.add_edge(2, 7, weight = 2)


print(G[1])
for nodi in G[1]:
    print(G[1][nodi]['weight'])
# G = nx.Graph([(1, 2, {"color": "yellow"})])
# print(G[1])
# G.add_edge(1, 2)
#
print(nx.shortest_path(G, source=None, target=None, weight=None, method='dijkstra'))
nx.draw(G)
plt.show()
