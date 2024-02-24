import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]  # Priority queue to store vertices based on distance from the source
    
    while pq:
        # Extract the vertex with the minimum distance from the priority queue
        d, u = heapq.heappop(pq)
        
        # Check if the extracted vertex's distance is already greater than the current shortest distance
        if d > dist[u]:
            continue
        
        # Update the shortest distance for each neighbor of the extracted vertex
        for v in range(n):
            if graph[u][v] != 0:  # Check if there's an edge between u and v
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    heapq.heappush(pq, (dist[v], v))  # Add v to the priority queue with its updated distance
                    
    return dist

# Given graph
G = [[0, 6, 0, 0, 0, 0, 0, 9, 0],
     [6, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [9, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]

source_node = 0 # Source node index

shortest_distances = dijkstra(G, source_node)
print("Shortest distances from source node {}:".format(source_node))
for i, distance in enumerate(shortest_distances):
    print("Node {}: {}".format(i, distance))
    
    
'''
output:

Shortest distances from source node 0:
Node 0: 0
Node 1: 6
Node 2: 14
Node 3: 21
Node 4: 22
Node 5: 12
Node 6: 10
Node 7: 9
Node 8: 16

'''
