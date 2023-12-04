from collections import defaultdict
def topological_sort(graph):
    visited = set()
    result = []
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    result.reverse()
    return result

graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [4]
graph[3] = [4, 5]
graph[4] = [6]
graph[5] = [6]
graph[6] = []

sorted_vertices = topological_sort(graph)
print(sorted_vertices)

