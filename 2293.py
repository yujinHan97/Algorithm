'''
    알고리즘:
    (다시 풀기, 링크 : https://www.youtube.com/watch?v=2IkdAk1Loek&t=543s)
    1. 1원으로는 모든 금액을 1번씩 만들 수 있다
    2. 만약 2원을 포함해서 4원을 만드려면, dp[2]의 각 경우에다가 2씩 붙이면 되니까, dp[i] = dp[i] + dp[i-coin]이 된다
'''
n, k = map(int, input().split())
coins = []
for i in range(n):
  coins.append(int(input()))

dp = [1] + [0 for i in range(k)]
for coin in coins:
  for i in range(1, k+1):
    if i - coin >= 0:
      dp[i] += dp[i-coin]

print(dp[k])
