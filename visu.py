import networkx as nx
import matplotlib.pyplot as plt

# Define the rooms and their connections
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

# Create a graph
G = nx.Graph()

# Add nodes and edges
for room, connections in terems.items():
    for connected_room in connections:
        G.add_edge(room, connected_room)

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
plt.title("Room Connections")
plt.show()
