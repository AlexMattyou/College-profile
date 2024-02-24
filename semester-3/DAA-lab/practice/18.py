import heapq

def solve_assignment(assignment_matrix):
    n = len(assignment_matrix)
    assigned_jobs = set()
    total_cost = 0

    # Define a priority queue to store partial solutions
    pq = [(0, [], 0)]  # (cost, assigned_jobs, current_row_index)

    while pq:
        cost, assigned, row = heapq.heappop(pq)

        if row == n:  # Reached the end of the matrix
            total_cost = cost
            assigned_jobs = assigned
            break

        for col in range(n):
            if col not in assigned:  # If job not already assigned
                new_cost = cost + assignment_matrix[row][col]
                if new_cost < total_cost:  # Pruning condition
                    heapq.heappush(pq, (new_cost, assigned + [col], row + 1))

    return total_cost, assigned_jobs

# Define the assignment matrix
assignment_matrix = [
    [10, 11, 5, 7],
    [6, 8, 9, 5],
    [5, 7, 10, 8],
    [7, 6, 8, 12]
]

# Solve the assignment problem
min_cost, assignment = solve_assignment(assignment_matrix)

# Display the optimal assignment and minimum cost
print("Minimum Cost:", min_cost)
for emp, job in enumerate(assignment):
    print(f"Employee{emp+1} -> Job{job+1}")


'''
program is wrong

expacted output:

Minimum Cost: 24
Optimal Assignment:

Employee1 -> Job3
Employee2 -> Job4
Employee3 -> Job2
Employee4 -> Job1

'''