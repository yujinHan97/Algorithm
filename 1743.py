'''
    알고리즘:
    1. graph를 지나가면서, 음식물이 있는 공간에서 bfs 수행
    2. bfs를 수행하면서, 상하좌우 음식물이 있으면 음식물의 크기를 증가시킨다
    3. 음식물의 크기를 return 하여 가장 큰 음식물 크기를 출력
'''
from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
  x, y = map(int, input().split())
  graph[x-1][y-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  q = deque()
  q.append((i, j))
  max_size = 1 # 초기 음식물 사이즈는 1
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 1:
          q.append((nx, ny))
          graph[nx][ny] = 0 # 붙어있는 음식물 처리를 했으니까 0으로 setting
          max_size += 1
          
  return max_size
  
res = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      graph[i][j] = 0
      res.append(bfs(i, j))

print(max(res))
