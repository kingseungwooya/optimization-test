import numpy as np
from scipy.optimize import milp, LinearConstraint

'cost의 계수 0 또는 1로'
cost_co = -np.array([0, 1], dtype=np.float32)

'다시 Ax=b 형태로'
A = np.array([
    [-1, 1],
    [3, 2],
    [2, 3]],
    dtype=np.float32
)
b_u = np.array([1, 12, 12])

'arg1의 모양으로 -infinity 넣어 만듬'
b_1 = np.full_like(b_u, -np.inf)

constraints = LinearConstraint(A=A, lb=b_1, ub=b_u)
# 정수형 안전빵
integrality = np.ones_like(cost_co)

# 실수형 해를 찾음 그러면 완전 바운더리에 걸치겠지?
# integrality = np.ones_like(cost_co)
integrality = np.array(
    [0, 1]  # y = integer x = 정수형이든 실수든 아무거나 이러면 x축은 완전 바운더리에 붙는다
)
bounds = [
    (0, None),
    (0, None)
]
result = milp(
    c=cost_co,
    integrality=integrality,
    # bounds=bounds,
    constraints=constraints
)
print(result)

