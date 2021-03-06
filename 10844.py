'''
    10844 쉬운 계단 수 
    알고리즘:
    1. dp[i][j] : i자리 수에서 마지막 자리에 숫자 j가 올 경우의 수
    2. j == 0인 경우, 앞이 무조건 1이어야 하고, 그 경우의 수는 [i-1][1]과 같다
    3. j == 9인 경우, 앞이 무조건 8이어야 하고, 그 경우의 수는 [i-1][8]과 같다
    4. j가  그 외 경우, 앞이 j-1이거나 j+1이어야하고, 그 경우의 수는 [i-1][j-1] + [i-1][j+1]과 같다
'''
N = int(input())
dp = [[0] * 10 for i in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)