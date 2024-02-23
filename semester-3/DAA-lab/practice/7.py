def warshall(graph):
    n = len(graph)
    closure = [[0]*n for _ in range(n)]  # Initialize the closure matrix with zeros

    # Initialize closure matrix to the adjacency matrix of the given graph
    for i in range(n):
        for j in range(n):
            closure[i][j] = graph[i][j]

    # Update closure matrix using Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

# Given graph
graph = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

# Find transitive closure using Warshall's algorithm
closure = warshall(graph)

# Print the transitive closure
print("Transitive Closure:")
for row in closure:
    print(row)


'''
output:

Transitive Closure:
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]

'''