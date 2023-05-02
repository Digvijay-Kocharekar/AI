import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['I', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': ['G'],
    'F': ['D', 'J'],
    'G': [''],
    'I': ['F'],
    'J': ['G']
}

# Create a directed graph object
G = nx.DiGraph(graph)

# Add node positions to the graph
pos = {
    'A': [0, 18],
    'B': [2, 13],
    'C': [1, 8],
    'D': [3, 6],
    'E': [4, 0],
    'F': [5, 12],
    'G': [6, 1],
    'I': [4, 15],
    'J': [6, 9]
}

# Draw the graph
nx.draw(G, pos, with_labels=True)
plt.show()