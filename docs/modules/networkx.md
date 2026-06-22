# NetworkX

NetworkX is a library for the creation, manipulation, and analysis of complex networks and graphs.

```python
import networkx as nx
```

## Creating a Graph

```python
# Create an empty undirected graph
G = nx.Graph()

# Create a directed graph
D = nx.DiGraph()
```

### Adding Nodes

```python
# Add a single node
G.add_node(1)
G.add_node("A", label="Node A", weight=5)

# Add multiple nodes
G.add_nodes_from([2, 3, 4, 5])
G.add_nodes_from([("B", {"label": "Node B"}), ("C", {"label": "Node C"})])
```

### Adding Edges

```python
# Add a single edge
G.add_edge(1, 2)
G.add_edge("A", "B", weight=4.5)

# Add multiple edges
G.add_edges_from([(1, 3), (2, 4), (3, 5)])

# Add weighted edges (node1, node2, weight)
G.add_weighted_edges_from([(1, 2, 3.0), (2, 3, 1.5), (3, 4, 2.0)])
```

### Removing Nodes and Edges

```python
# Remove a single node (also removes its edges)
G.remove_node(5)

# Remove multiple nodes
G.remove_nodes_from([4, 5])

# Remove edges
G.remove_edge(1, 2)
G.remove_edges_from([(1, 3), (2, 4)])
```

## Graph Information

```python
# Nodes and edges
print(G.nodes())            # List of all nodes
print(G.edges())            # List of all edges
print(G.edges(data=True))   # Edges with attributes

# Neighbours of a node
print(list(G.neighbors(1)))

# Check existence
print(G.has_node(1))        # True/False
print(G.has_edge(1, 2))     # True/False

# Counts
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.size())             # Number of edges (or sum of weights if weighted)
```

| Method | Description |
|--------|-------------|
| `G.nodes()` | All nodes in the graph |
| `G.edges()` | All edges in the graph |
| `G.neighbors(n)` | Nodes adjacent to node `n` |
| `G.has_node(n)` | Check if node exists |
| `G.has_edge(u, v)` | Check if edge exists |
| `G.number_of_nodes()` | Count of nodes |
| `G.number_of_edges()` | Count of edges |
| `G.size()` | Number of edges |
| `G.degree(n)` | Degree of node `n` |

## Graph Functions

### Connected Components

```python
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 5)])

# Get connected components (sets of nodes)
components = list(nx.connected_components(G))
print(components)  # [{1, 2, 3}, {4, 5}]

# Number of connected components
print(nx.number_connected_components(G))  # 2
```

!!! warning "Removed: connected_component_subgraphs"
    `nx.connected_component_subgraphs(G)` was removed in NetworkX 2.4. Use this pattern instead:
    ```python
    for component in nx.connected_components(G):
        subgraph = G.subgraph(component).copy()
        # work with subgraph
    ```

### Isolates

Isolates are nodes with no edges.

```python
G.add_node(99)  # Node with no connections
isolates = list(nx.isolates(G))
print(isolates)  # [99]

# Remove all isolates
G.remove_nodes_from(list(nx.isolates(G)))
```

### Shortest Path (Dijkstra)

```python
G = nx.Graph()
G.add_weighted_edges_from([
    ("A", "B", 1),
    ("B", "C", 2),
    ("A", "C", 4),
    ("C", "D", 1),
])

# Bidirectional Dijkstra (returns length and path)
length, path = nx.bidirectional_dijkstra(G, "A", "D")
print(f"Shortest path: {path}")     # ['A', 'B', 'C', 'D']
print(f"Total weight: {length}")    # 4

# Simple shortest path
path = nx.shortest_path(G, "A", "D", weight="weight")
print(path)  # ['A', 'B', 'C', 'D']
```

## Complete Example

```python
import networkx as nx

# Build a social network
G = nx.Graph()
G.add_edges_from([
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "David"),
    ("Eve", "Frank"),
])

# Basic stats
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Connected components: {nx.number_connected_components(G)}")

# Find the largest component
largest = max(nx.connected_components(G), key=len)
print(f"Largest component: {largest}")

# Shortest path between two people
if nx.has_path(G, "Alice", "David"):
    path = nx.shortest_path(G, "Alice", "David")
    print(f"Path from Alice to David: {path}")
```
