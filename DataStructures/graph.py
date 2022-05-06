"""
Runbook:
python3 -i graph.py
adjacency_dict(G)
adjacency_matrix(G)
"""
 
from collections import namedtuple
 
# namedtuple allows you to name type and its components (similar to user-defined class)
Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])
 
nodes = [0, 1, 2]
 
edges = [(1, 0),
        (1, 2),
        (0, 2)
        ]
 
# if directed, we only get edge in one direction, not both
directed = False
 
G = Graph(nodes, edges, directed)
 
 
def adjacency_dict(graph):
   """
   Returns the adjacency list representation of the graph.
   In adj dict, the keys are nodes of graph, and values are lists of adjacent nodes.
   Consequence of using dict for representation: nodes must be hashable & immutable such as string, int.
   """
   # list comprehension to build dict; initialize each value as empty list
   adj = {node: [] for node in graph.nodes}
   for edge in graph.edges:
       # edge starts at node1 and ends at node2 if directed
       node1, node2 = edge[0], edge[1]
       adj[node1].append(node2)
       if not graph.is_directed:
           adj[node2].append(node1)
   return adj
 
 
def adjacency_matrix(graph):
   """
   Returns the adjacency matrix of the graph.
   A matrix is a 2D array, so we represent using a list of lists.
   Each list is a row in the adjacency matrix.
   Each value in list is number of edges.
 
   Assumes that graph.nodes is equivalent to range(len(graph.nodes))
   (nodes must be int, not string) in order to use node names to index graph.
   """
   adj = [[0 for node in graph.nodes] for node in graph.nodes]
   for edge in graph.edges:
       node1, node2 = edge[0], edge[1]
       adj[node1][node2] += 1
       if not graph.is_directed:
           adj[node2][node1] += 1
   return adj
 
if __name__ == '__main__':
    print(adjacency_dict(G))
    print(adjacency_matrix(G))