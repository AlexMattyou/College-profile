def dfs_topological(graph, vertex, visited, stack):
    visited.add(vertex)  # Mark the current vertex as visited

    # Visit all adjacent vertices of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_topological(graph, neighbor, visited, stack)  # Recursive call to visit the neighbor vertex

    stack.append(vertex)  # Add the current vertex to the stack after visiting all its neighbors


def topological_sort(graph):
    visited = set()  # Create a set to store visited vertices
    stack = []  # Stack to store topological order

    # Perform DFS traversal for each vertex in the graph
    for vertex in graph:
        if vertex not in visited:
            dfs_topological(graph, vertex, visited, stack)

    return stack[::-1]  # Return the reversed stack to get the topological order


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'E'],
    'B': ['C'],
    'C': [],
    'D': ['A','B','C','E','G'],
    'E': ['G','F'],
    'F': [],
    'G': ['C','F']
}

print("Topological Sorting Order:")
print(topological_sort(graph))
