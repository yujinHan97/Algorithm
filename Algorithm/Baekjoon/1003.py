'''
    1003 피보나치 함수
    알고리즘:
    1. N에 따라 0호출과 1호출을 세보았다
       N : 0    1   2   3   4   5   6
       0 : 1    0   1   1   2   3   5
       1 : 0    1   1   2   3   5   8
    2. 0호출도 피보나치 수열, 1호출도 피보나치 수열을 이루었다
'''
T = int(input())
for i in range(T):
    N = int(input()) 
    zero = [1, 0]
    one = [0, 1]

    for i in range(2, N+1):
        zero.append(zero[i-2] + zero[i-1])
        one.append(one[i-2]+one[i-1])
    
    print(zero[N], one[N])