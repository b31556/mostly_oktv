import networkx as nx
#import matplotlib.pyplot as plt

g = nx.Graph()

terems = {
    1: [3, 4, 5],
    2: [3, 4, 8],
    3: [1, 2, 8],
    4: [1, 2, 6],
    5: [1, 6],
    6: [4, 5, 7],
    7: [6],
    8: [2, 3]
}

for key in terems:
    for r in terems[key]:
        g.add_edge(key,r)

print(nx.shortest_path(g,7,1))