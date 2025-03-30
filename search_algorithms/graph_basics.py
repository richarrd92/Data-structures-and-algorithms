from collections import defaultdict, deque
from data import adj_matrix, nodes

# make adjacency list
def makeAdjList(matrix, labels) -> dict:
    adj_list = defaultdict(list)
    
    for v in range(len(matrix)):
        for u in range(len(matrix)):
            if matrix[v][u] == 1:
                adj_list[labels[v]].append(labels[u])
    return dict(adj_list)
    
# print adjacency list
def printAdjList(adj):
    for key in adj.keys():
        print(key, " : ", adj[key])


# Breadth-First Search (BFS) from Node A:
# What is the order of traversal if you perform BFS starting from node A?
# Expected Answer: A, B, C, D, E, F, G (or equivalent ordering depending on queue processing).

# BFS algorithm
def bfs(adjacency_list: dict, start: str) -> list:
    q = deque(start) # initialize queue and append start node
    visited = set() # visited nodes

    path = [] # track path
    
    # traverse
    while q:
        node = q.popleft()
        # node not visited
        if node not in visited:
            visited.add(node)
            path.append(node) # add node to path
            # add neighbors
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    q.append(neighbor)

    return path


# Depth-First Search (DFS) from Node A:
# What is the order of traversal if you perform DFS starting from node A?
# Expected Answer: A, B, C, E, D, F, G (one possible order, depending on stack processing).

# DFS algorithm
def dfs(adjacency_list: dict, start: str) -> list:
    stack = [start] # initialize stack and append start node
    visited = set() # visited nodes

    path = [] # track path
    
    # traverse
    while stack:
        node = stack.pop()
        # node not visited
        if node not in visited:
            visited.add(node)
            path.append(node) # add node to path
            # add neighbors
            # add neighbors in reverse order to maintain left-to-right processing
            for neighbor in reversed(adjacency_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return path


# Find the shortest path from A to G using BFS:
# What is the shortest path from A to G?
# Expected Answer: A → C → E → G (or an equivalent valid shortest path).

# returns the shorstest path -> list
def shortest_path(adjacency_list: dict, start: str, end: str) -> list:
    # implement using bfs 
    q = deque([(start, [start])])  # Queue holds tuples: (current_node, path_so_far)
    visited = set()

    while q:
        node, path = q.popleft() # dynamic path creation from each node
        # shortest path found - BFS properties
        if node == end:
            return path
        # node not visited
        if node not in visited:
            visited.add(node)
            # add neighbors 
            for neighbor in adjacency_list[node]:
                 if neighbor not in visited:
                    q.append((neighbor, path + [neighbor]))  # Append the new path with the neighbor
    return []

print("ADJACENCY LIST:\n")
adj_list = makeAdjList(adj_matrix, nodes)
printAdjList(adj_list)
bfs_path = bfs(adj_list, "A")
print("\nBFS Traversal: ", bfs_path)
dfs_path = dfs(adj_list, "A")
print("DFS Traversal: ", bfs_path)
min_path = shortest_path(adj_list, "A", "G")
print("The shortest path from A to G: ", min_path)

# Find all connected components in the graph:
# How many connected components does this graph have?
# Expected Answer: 1 (the entire graph is connected).

# Check if the graph contains a cycle:
# Does the graph have a cycle?
# Expected Answer: Yes, since nodes are interconnected forming multiple cycles.

# Find all nodes at distance 2 from A:
# Which nodes are exactly 2 edges away from A?
# Expected Answer: {D, E}

# Topological Sorting Feasibility:
# Can this graph be topologically sorted?
# Expected Answer: No, because it contains cycles.