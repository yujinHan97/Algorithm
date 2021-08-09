'''
    11051 이항계수
    알고리즘:
    1. factorial 라이브러리 사용
'''
from math import factorial

N, K = map(int, input().split())
value = factorial(N) // (factorial(K) * factorial(N-K))
print(value % 10007)