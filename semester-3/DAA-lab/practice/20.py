
adj_matrix = [
    [0, 1, 3, 8],
    [1, 0, 7, 5],
    [3, 7, 0, 2],
    [8, 3, 2, 0]
]

# Function to convert adjacency matrix to adjacency list
def adjacency_matrix_to_list(matrix):
    n = len(matrix)
    adj_list = [[] for _ in range(n)]  # Initialize empty adjacency list for each vertex

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:  # Check if there's an edge between vertex i and vertex j
                adj_list[i].append((j, matrix[i][j]))  # Add (vertex, weight) tuple to adjacency list

    return adj_list

# Convert adjacency matrix to adjacency list
adj_list = adjacency_matrix_to_list(adj_matrix)

# Function to calculate the cost of a tour
def calculate_tour_cost(tour, adj_list):
    cost = 0
    for i in range(len(tour) - 1):
        u, v = tour[i], tour[i + 1]
        for neighbor, weight in adj_list[u]:
            if neighbor == v:
                cost += weight
                break
    return cost

# Function to solve TSP using Branch and Bound
def tsp_branch_and_bound(adj_list):
    n = len(adj_list)
    min_cost = float('inf')
    min_tour = None

    def dfs(node, visited, path, cost):
        nonlocal min_cost, min_tour
        if len(path) == n:
            if cost < min_cost:
                min_cost = cost
                min_tour = path[:]
        else:
            for neighbor, weight in adj_list[node]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    if new_cost < min_cost:
                        dfs(neighbor, visited.union({neighbor}), path + [neighbor], new_cost)

    for i in range(n):
        dfs(i, {i}, [i], 0)

    return min_cost, min_tour

# Solve TSP using Branch and Bound
min_cost, min_tour = tsp_branch_and_bound(adj_list)

# Print the minimum cost and corresponding tour
print("Minimum Cost:", min_cost)
print("Minimum Tour:", min_tour)

'''
<- sorry the output is wrong - >
program is also wrong

Minimum Cost: 11
tour = find it by yourself
'''
