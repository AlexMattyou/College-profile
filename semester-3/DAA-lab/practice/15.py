from scipy.optimize import linprog

# Objective function coefficients
c = [-63, -90]  # negative because linprog minimizes by default

# Coefficients of inequality constraints (left-hand side)
A = [
    [60, 110],  # Total expenses constraint
    [110, 40]   # Total storage space constraint
]

# Right-hand side of the inequality constraints
b = [30000, 20200]

# Bounds for variables x1 and x2 (non-negativity constraints)
x0_bounds = (0, None)  # x1 >= 0
x1_bounds = (0, None)  # x2 >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract solution
acres_of_corn_planted = result.x[0]
acres_of_soybeans_planted = result.x[1]
max_profit = -result.fun  # convert back to positive because of the negation

# Print solution
print("Solution:")
print("Acres of corn planted:", acres_of_corn_planted)
print("Acres of soybeans planted:", acres_of_soybeans_planted)
print("Maximum profit: $", max_profit)


'''
output:

Solution:
Acres of corn planted: 105.36082474226805
Acres of soybeans planted: 215.2577319587629
Maximum profit: $ 26010.92783505155


'''