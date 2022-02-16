'''
    알고리즘:
    1. 왼쪽 위, 왼쪽, 왼쪽 아래에서 오는 것의 최대를 구하여 dp 테이블 갱신
    2. j == 0일때, j == n-1일때의 경우는 따로 분리하여 범위 벗어나지 않도록 구현
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  graph = []
  n, m = map(int, input().split())
  temp = list(map(int, input().split()))
  for i in range(n):
    temp_row = temp[i*m:(i+1)*m]
    graph.append(temp_row)

  dp = [[0] * m for _ in range(n)]
  for i in range(n):
    dp[i][0] = graph[i][0]

  for i in range(1, m):
    for j in range(n):
      if j == 0:
        dp[j][i] = graph[j][i] + max(dp[j][i-1], dp[j+1][i-1])
      elif j == n-1:
        dp[j][i] = graph[j][i] + max(dp[j-1][i-1], dp[j][i-1])
      else:
        dp[j][i] = graph[j][i] + max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1])

  max_dp = []
  for i in range(n):
    max_dp.append(dp[i][m-1])

  print(max(max_dp))
