'''
    알고리즘:
    1. 2중 for문 돌면서 i번째 일에 상담 할 수 있으면 하기
    2. i번째 상담을 할 경우, 이전에 어떤 상담할지 고르기 위해 j로 돌면서 최대이익 maxdp 찾기
'''
n = int(input())
t = [0]
p = [0]
for i in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)
  
dp = [0] * (n+1)
for i in range(1, n+1):
  # 해당 일자 상담을 못하는 경우 그냥 무시
  if (i-1) + t[i] > n:
    continue

  # 상담 가능한 경우, 당일 상담을 일단 하고
  dp[i] += p[i]

  # 전에 어떤 상담들을 할지 결정하기
  maxdp = 0
  for j in range(1, i):
    if j + t[j] <= i:
      if maxdp < dp[j]: # 가장 큰 이익을 얻을 수 있는 상담 고르기
        maxdp = dp[j]
  dp[i] += maxdp
  
print(max(dp))
