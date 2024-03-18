import numpy as np
from scipy import optimize
import math

'''
    2024-03-18 : 컬럼의 가격 및 제작 비용을 뜻하는 목적 함수임
'''
def objective(x):
    return 9.82*x[0]*x[1] + 2.0*x[0]

'''
    제약 조건들
'''
def constraint_yield_stress(x):
    return 500 - 2500/(math.pi*x[0]*x[1])

def  constraint_buckling_stress(x):
    return math.pi**2 * 0.85e+6 * (x[0] * x[0] + x[1] * x[1]) / (8 * (250 ** 2)) - 2500/(math.pi * x[0] * x[1])

# 설계 변수의 초기값
x0 = [10.0, 0.2]

# 경게값
bounds = ((2, 14), (0.2, 0.8))

constraints = (
    {
        'type': 'ineq',
        'fun': constraint_yield_stress
     },
    {
        'type': 'ineq',
        'fun': constraint_buckling_stress
    }
)

result = optimize.minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
print(result)

# 제약조건에 정답을 넣었을 때 0에 가깝다면 activate constraint 이다.
# 두개에 0에 가까워진 값을 찾는게 최적화다.
print(constraint_yield_stress(result.x))
print(constraint_buckling_stress(result.x))
