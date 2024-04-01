"""
minimize
c @ x
such that
A_ub @ x <= b_ub
A_eq @ x == b_eq
lb <= x <= ub
"""
import numpy as np
from scipy.optimize import linprog

c = np.array([29, 45, 0, 0])  # max = 29x1 + 45x2
A_ub = np.array([
    [1, -1, -3, 0],
    [-2, 3, 7, -3]
])
b_ub = np.array([5, -10])
A_eq = np.array([
    [2, 8, 1, 0],
    [4, 4, 0, 1]
])
b_eq = np.array([60, 60])
'''
0<=x1
0<=x2<=5
x3<=0.5
-3<=x3
'''
bounds = np.array([
    [0, None],
    [0, 6],
    [None, 0.5],
    [-3, None]
])

result = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)
print(result)
