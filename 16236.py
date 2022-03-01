'''
    알고리즘:
    (거의 비슷하게 풀었으나, find 함수부분을 제대로 구현하지 못함)
    1. bfs를 이용해서 거리를 구하고 최소 거리에 있는 물고기들을 먹는다
    2. 물고기를 먹고난 뒤에는, 빈칸으로 처리하고 상어의 위치를 바꾸고 size조건을 만족하면 크기를 
'''
from collections import deque
INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] == 9:
      s_x, s_y = i, j # 아기 상어의 위치 저장
      graph[i][j] = 0

shark_size = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
  q = deque()
  q.append([s_x, s_y])
  distance = [[INF for i in range(n)] for i in range(n)]
  distance[s_x][s_y] = 0
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] <= shark_size and distance[nx][ny] == INF:
          distance[nx][ny] = min(distance[nx][ny], distance[x][y] + 1)
          q.append((nx, ny))

  return distance 

# 최단거리가 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
  x, y = 0, 0
  min_dist = INF

  for i in range(n):
    for j in range(n):
      if dist[i][j] != INF and 1 <= graph[i][j] < shark_size:
        if dist[i][j] < min_dist:
          min_dist = dist[i][j]
          x, y = i, j

  if min_dist == INF:
    return None
  else:
    return x, y, min_dist
  
answer, count = 0, 0 # count : 먹은 물고기 수
while True:
  temp = find(bfs())
  if temp == None:
    print(answer)
    break
  else:
    s_x, s_y = temp[0], temp[1]
    answer += temp[2]
    graph[s_x][s_y] = 0
    count += 1
    
    if count >= shark_size:
      shark_size += 1
      count = 0
