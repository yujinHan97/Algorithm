''' 
    10872 팩토리얼
    알고리즘 : 
    1. 재귀 이용, N <= 1인 경우 종료조건
'''
N = int(input())

def factorial(N):
    if N <= 1:
        return 1
    else :
        return N * factorial(N-1)

result = factorial(N)
print(result)