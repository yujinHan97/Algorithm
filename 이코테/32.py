'''
    알고리즘:
    1. 위에서 아래로 내려오는데, 왼쪽 위, 바로위 2가지 중 큰 수를 채택해서 더하여 dp 테이블 갱신
    2. 인덱스 범위 벗어나지 않기 위해서, 가장 가장자리 부분은 따로 경우를 나눔
'''
n = int(input())
tri = []
for _ in range(n):
  tri.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = tri[0][0]

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      dp[i][j] = tri[i][j] + dp[i-1][0]
    elif j == i:
      dp[i][j] = tri[i][j] + dp[i-1][j-1]
    else:
      dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
