'''
    2193 이친수
    알고리즘:
    1. N에 따라 가짓수를 나열해본다
        N = 1   1 (1)
        N = 2   10 (1)
        N = 3   100 101 (2) 
        N = 4   1000 1001 1010 (3) 
        N = 5   10000 10001 10010 10100 10101 (5)
    2. N에따른 가짓수는 피보나치 수열을 이룬다
'''
dp = [0] * 91
def fibo(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    
    if dp[N] != 0:
        return dp[N]
    
    dp[N] = fibo(N-1) + fibo(N-2)
    return dp[N]

N = int(input())
print(fibo(N))