N = int(input())
tri = []
dp = [[0] *N for i in range(N)]
for i in range(N):
    tri.append(list(map(int, input().split())))
    if i == 0:
        dp[i][0] = tri[i][0]
    
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        
        if i == j:
            dp[i][j] = dp[i-1][j] + tri[i][j]

        dp[i][j] = max(dp[i-1][j-1]+tri[i][j], dp[i-1][j] +tri[i][j])

max_value = 0
for i in range(N):
    for j in range(i+1):
        if dp[i][j] > max_value:
            max_value = dp[i][j]

print(max_value)