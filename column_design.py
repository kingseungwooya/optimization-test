import numpy as np
from scipy import optimize
import math

'''
    2024-03-18 : 컬럼의 가격 및 제작 비용을 뜻하는 목적 함수임
'''


def objective(x):
    return 9.82 * x[0] * x[1] + 2.0 * x[0]


def gradient_objective(x):
    return [9.82 * x[1] + 2.0, 9.82 * x[0]]


'''
    제약 조건들
'''


def constraint_yield_stress(x):
    return 500 - 2500 / (math.pi * x[0] * x[1])


def constraint_buckling_stress(x):
    return math.pi ** 2 * 0.85e+6 * (x[0] * x[0] + x[1] * x[1]) / (8 * (250 ** 2)) - 2500 / (math.pi * x[0] * x[1])


def constraint_gradient_yield_stress(x):
    return [2500 / (math.pi * x[0] ** 2 * x[1]), 2500 / (math.pi * x[0] * x[1] ** 2)]


def constraint_gradient_buckling_stress(x):
    return [(math.pi ** 2 * 0.85e+6 * x[0]) / (4 * 250 ** 2) + (2500) / (math.pi * x[1] * x[0] ** 2),
            (math.pi ** 2 * 0.85e+6 * x[1]) / (4 * 250 ** 2) + (-2500) / (math.pi * x[0] * x[1] ** 2)]


# 설계 변수의 초기값
x0 = [10.0, 0.2]

# 경게값
bounds = ((2, 14), (0.2, 0.8))

constraints = (
    {
        'type': 'ineq',
        'fun': constraint_yield_stress,
        'jac': constraint_gradient_yield_stress
    },
    {
        'type': 'ineq',
        'fun': constraint_buckling_stress,
        'jac': constraint_gradient_buckling_stress
    }
)

result = optimize.minimize(objective, x0, jac=gradient_objective, method='SLSQP', bounds=bounds,
                           constraints=constraints)
print(result)
# result 의 jac가 0 이 아니라면 최적점 x 경계값에 걸림을 의미 -> 경계조건에 넣으면 0이 됌
# 제약조건에 정답을 넣었을 때 0에 가깝다면 activate constraint 이다.
# 두개에 0에 가까워진 값을 찾는게 최적화다.
print(constraint_yield_stress(result.x))
print(constraint_buckling_stress(result.x))
