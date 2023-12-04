import numpy as np

def simplex_method(c, A, b):
    m, n = len(A), len(c)
    tableau = np.zeros((m + 1, m + n + 2))
    tableau[:-1, :n] = A
    tableau[:-1, -2] = 1
    tableau[:-1, -1] = b
    tableau[-1, :n] = c
    tableau[-1, -2] = -1
    while np.any(tableau[-1, :-2] < 0):
        pivot_column = np.argmin(tableau[-1, :-2])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_column]
        pivot_row = np.argmin(ratios)
        pivot_element = tableau[pivot_row, pivot_column]
        tableau[pivot_row, :] /= pivot_element
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_column] * tableau[pivot_row, :]
    optimal_value = -tableau[-1, -1]
    optimal_solution = tableau[:-1, -1]
    return optimal_value, optimal_solution

c = np.array([-2, -3])
A = np.array([[1, 1], [2, 1]])
b = np.array([4, 5])
optimal_value, optimal_solution = simplex_method(c, A, b)

print("Optimal value:", optimal_value)
print("Optimal solution:", optimal_solution)