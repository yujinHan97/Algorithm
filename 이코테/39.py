# 풀이 1 : BFS
'''
    알고리즘:
    1. 상하좌우 거리를 갱신해가면서, 값을 갱신했으면 q에 넣고 다시 반복
'''
from collections import deque
def bfs(i, j):
  q = deque([])
  q.append((i, j))
  dist[i][j] = mars[i][j]
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        temp = mars[nx][ny] + dist[x][y]
        if temp < dist[nx][ny]:
          dist[nx][ny] = temp
          q.append((nx, ny))
          
t = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(t):
  n = int(input())
  mars = []
  INF = int(1e9)
  dist = [[INF for i in range(n)] for i in range(n)]
  
  for i in range(n):
    mars.append(list(map(int, input().split())))

  bfs(0, 0)

  print(dist[n-1][n-1])

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 풀이 2 : 다익스트라
'''
    알고리즘:
    1. 다익스트라로(BFS와 코드는 비슷), 이미 처리가 된 노드라면 무시하고 되지 않았다면 최단 경로로 갱신 
'''
import heapq, sys
input = sys.stdin.readline

t = int(input())
INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(t):
  n = int(input())
  mars = []

  for i in range(n):
    mars.append(list(map(int, input().split())))

  dist = [[INF for i in range(n)] for i in range(n)]
  x, y = 0, 0
  q = [(mars[x][y], x, y)] # 비용과 시작점 설정하여 큐에 삽입
  dist[x][y] = mars[x][y]

  # 다익스트라 수행
  while q:
    cost, x, y = heapq.heappop(q)

    if dist[x][y] < cost:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0<= nx < n and 0<= ny < n:
        temp = cost + mars[nx][ny]
        if temp < dist[nx][ny]:
          dist[nx][ny] = temp
          heapq.heappush(q, (temp, nx, ny))
  
  print(dist[n-1][n-1])
