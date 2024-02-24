def floyd_warshall(graph):
    n = len(graph)
    # Initialize the distance matrix with the adjacency matrix
    distance = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Iterate over intermediate vertices
    for k in range(n):
        # Iterate over all pairs of vertices (i, j)
        for i in range(n):
            for j in range(n):
                # Update distance[i][j] if there's a shorter path passing through vertex k
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Given adjacency matrix
graph = [
    [0, 5, float('inf'), float('inf'), 10, float('inf')],
    [float('inf'), 0, 7, 12, float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, 8, float('inf'), float('inf')],
    [3, float('inf'), float('inf'), 0, 9, 6],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, 20],
    [float('inf'), float('inf'), 15, float('inf'), float('inf'), 0]
]

# Compute shortest paths using Floyd's Algorithm
shortest_paths = floyd_warshall(graph)

# Print shortest paths
print("Shortest Paths between Every Pair of Vertices:")
for row in shortest_paths:
    print(row)

'''
output:

Shortest Paths between Every Pair of Vertices:
[0, 5, 12, 17, 10, 23]
[15, 0, 7, 12, 21, 18]
[11, 16, 0, 8, 17, 14]
[3, 8, 15, 0, 9, 6]
[46, 51, 35, 43, 0, 20]
[26, 31, 15, 23, 32, 0]

'''