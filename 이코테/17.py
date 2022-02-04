'''
    알고리즘:
    1. 번호가 낮은 종류가 먼저 전염되니까, 번호를 기준으로 정렬 후 bfs
    2. q에 대해서, 전염이 일어나지 않은곳이라면 전염 시킴. 
'''
from collections import deque

n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j], 0, i, j))
s, x, y = map(int, input().split())

# 번호가 낮은 종류의 바이러스로 정렬
virus.sort(key = lambda x:x[0])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# bfs
q = deque(virus)
while q:
  v_sp, sec, c_x, c_y = q.popleft()

  if sec == s:
    break

  for i in range(4):
    nx = c_x + dx[i]
    ny = c_y + dy[i]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    
    if graph[nx][ny] == 0:
      graph[nx][ny] = v_sp
      q.append((v_sp, sec+1, nx, ny))

print(graph[x-1][y-1])
