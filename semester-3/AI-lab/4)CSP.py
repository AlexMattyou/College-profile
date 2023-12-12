def is_cons(var, val, assign):
    for neigh in graph[var]:
        if neigh in assign and assign[neigh] == val:
            return False
    return True

def backtrack(assign):
    if len(assign) == len(regions):
        return assign

    var = select_unassigned(assign)
    for val in domain:
        if is_cons(var, val, assign):
            assign[var] = val
            result = backtrack(assign)
            if result is not None:
                return result
            del assign[var]
    return None

def select_unassigned(assign):
    unassigned_vars = [v for v in regions if v not in assign]
    return min(unassigned_vars, key=lambda v: len(graph[v]))

def print_sol(sol):
    for reg, col in sol.items():
        print(f"Region {reg} is colored {col}")

graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
regions = list(graph.keys())
domain = ['Red', 'Green', 'Blue']

sol = backtrack({})
if sol is not None:
    print_sol(sol)
else:
    print("No solution found.")
    
    