n, m = map(int, input().split())

coins = []
INF = int(1e9)
dp = [INF] * (10001)
for i in range(n):
  cur = int(input())
  coins.append(cur)
  dp[cur] = 1

# for i in range(1, m+1):
#   temp = []
#   if dp[i] == 1:
#     continue
#   for coin in coins:
#     if i - coin > 0:
#       temp.append(dp[i-coin] + 1) 
      
#   if len(temp) > 0:
#     dp[i] = min(temp)

# 주석부분을 더 효율적으로 고친 코드!
for i in range(1, m+1):
  for coin in coins:
    if i -coin > 0:
      dp[i] = min(dp[i], dp[i-coin]+1)
      
if dp[m] >= INF:
  print(-1)
else:
  print(dp[m])
