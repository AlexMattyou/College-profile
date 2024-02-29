import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start, end, cost):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, cost))

def astar(graph, start, goal, heuristic):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            break

        for next_node, cost in graph.edges[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current_node

    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start)
    path.reverse()

    return path

# Example usage:

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])  # Manhattan distance heuristic

graph = Graph()
graph.add_edge((0, 0), (0, 1), 1)
graph.add_edge((0, 1), (0, 2), 1)
graph.add_edge((0, 2), (1, 2), 1)
graph.add_edge((1, 2), (2, 2), 1)
graph.add_edge((2, 2), (2, 1), 1)
graph.add_edge((2, 1), (2, 0), 1)
graph.add_edge((2, 0), (1, 0), 1)
graph.add_edge((1, 0), (0, 0), 1)

start = (0, 0)
goal = (2, 2)

path = astar(graph, start, goal, heuristic)
print("Path:", path)
