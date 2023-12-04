import sys

def tsp(graph):
    cities = list(graph.keys())
    n = len(cities)
    visited = {city: False for city in cities}
    path = []
    minCost = sys.maxsize
    def tspUtil(cPath, cCost, cCity):
        nonlocal minCost, path
        if len(cPath) == n:
            if cCost < minCost:
                minCost = cCost
                path = cPath[:]
            return
        for neighbor, cost in graph[cCity].items():
            if not visited[neighbor]:
                visited[neighbor] = True
                cPath.append(neighbor)
                tspUtil(cPath, cCost + cost, neighbor)
                visited[neighbor] = False
                cPath.pop()
    startCity = cities[0]
    visited[startCity] = True
    tspUtil([startCity], 0, startCity)
    return path, minCost

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

bestPath, bestCost = tsp(graph)

print("Best Tour:", bestPath + [bestPath[0]])
print("Best Cost:", bestCost)
