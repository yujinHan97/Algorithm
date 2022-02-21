'''
    알고리즘:
    1. 마지막 날부터 전날까지 할 수 있는 상담은 최대로 한다 
    2. 점화식을 dp[i+t[i]]로 해서, 이후의 날짜들에 p를 더한다
'''
n = int(input())
t, p = [], []
dp = [0] * (n+1)
for i in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

for i in range(n-1, -1, -1):
  if i + t[i] > n:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(dp[0])
