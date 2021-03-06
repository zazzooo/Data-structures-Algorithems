import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
#
# G = nx.Graph()
#
# G.add_nodes_from(range(1,10))
# G.add_edge(1, 2, weight = 3)
# G.add_edge(4, 2, weight = 2.4)
# G.add_edge(6, 2,weight = 5)
# G.add_edge(4, 1,weight = 5)
# G.add_edge(1, 8, weight = 6)
# G.add_edge(3, 6,weight = 1)
# G.add_edge(2, 7, weight = 2)
# G.add_edge(9, 7, weight = 2)
# G.add_edge(10, 7, weight = 2)
# G.add_edge(2, 7, weight = 2)
#
#
# print(G[1])
# for nodi in G[1]:
#     print(G[1][nodi]['weight'])
# # G = nx.Graph([(1, 2, {"color": "yellow"})])
# # print(G[1])
# # G.add_edge(1, 2)
# #
# print(len(list(nx.simple_cycles(G))))
#
# print(nx.shortest_path(G, source= 1, target=7, weight=None, method='dijkstra'))
# G = nx.petersen_graph()

nodes = spark.read.csv("data/airports.csv", header=False)
cleaned_nodes = (nodes.select("_c1", "_c3", "_c4", "_c6", "_c7")
 .filter("_c3 = 'United States'")
 .withColumnRenamed("_c1", "name")
 .withColumnRenamed("_c4", "id")
 .withColumnRenamed("_c6", "latitude")
 .withColumnRenamed("_c7", "longitude")
 .drop("_c3"))
cleaned_nodes = cleaned_nodes[cleaned_nodes["id"] != "\\N"]

nx.draw(G)
plt.show()
