import networkx as nx
import matplotlib.pyplot as plt

Vertices = ['Olivia Doktor', 'Celine Müh', 'Winston Politikacı', 'Chloe Mimar', 'John Tamirci', 'Jack Prof']

Edges = [('Olivia Doktor', 'Celine Müh', 8), ('Olivia Doktor', 'Jack Prof', 4),
         ('Olivia Doktor', 'John Tamirci', 7), ('John Tamirci', 'Jack Prof', 9),
         ('John Tamirci', 'Chloe Mimar', 7), ('Chloe Mimar', 'Jack Prof', 5),
         ('Chloe Mimar', 'Winston Politikacı', 11), ('Winston Politikacı', 'Jack Prof', 7),
         ('Winston Politikacı', 'Celine Müh', 6), ('Celine Müh', 'Jack Prof', 5)]

G = nx.Graph()
G.add_nodes_from(Vertices)
G.add_weighted_edges_from(Edges)

pos = {'Olivia Doktor': [1, 3], 'Celine Müh': [3, 3], 'Winston Politikacı': [4, 2], 'Chloe Mimar': [1, 1],
       'John Tamirci': [0, 2], 'Jack Prof': [2, 2]}
weight = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='blue', edge_color='black', font_size=14)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight, font_size=15)

print("Dijkstra Path")
for i in range(len(Vertices)):
    for j in range (i + 1, len(Vertices)):
        print(nx.dijkstra_path(G, Vertices[i], Vertices[j]), nx.dijkstra_path_length(G, Vertices[i], Vertices[j]))

start_node_dfs = 'John Tamirci'
dfs_path = list(nx.dfs_edges(G, source=start_node_dfs))
print("DFS Dolaşımı:", dfs_path)

start_node_bfs = 'John Tamirci'
bfs_path = list(nx.bfs_edges(G, source=start_node_bfs))
print("BFS Dolaşımı:", bfs_path)
plt.show()