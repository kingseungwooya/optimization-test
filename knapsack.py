import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

# 물건의 가치
values = -np.array([22, 12, 16, 10, 35, 26, 42, 53])
# 물건의 무게
weights = [21, 12, 15, 9, 34, 25, 41, 52]

# 배낭의 용량
capacity = 100

# 이진 변수 (물건을 넣을지 말지)
Bounds(0, 1)
integrality = np.full_like(values, True)


# 제한 조건의 계수 행렬
A = [[weights[0], weights[1], weights[2]]]  # 물건의 무게
b = [capacity]  # 배낭의 용량

constraints = LinearConstraint(A=weights, lb=0, ub=capacity)


result = milp(
    c=values,
    integrality=integrality,
    constraints=constraints
)
print(result)