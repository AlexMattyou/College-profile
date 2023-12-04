def warshall(graph):
    n = len(graph)
    reach = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == j) or (graph[i][j] != 0):
                reach[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])  
    return reach

def floyd(graph):
    n = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

print("Warshall's:",warshall(graph))
print("Floyd's:",floyd(graph))

