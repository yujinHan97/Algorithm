'''
    알고리즘: 
    1. 가중치가 있는 최단 비용거리 -> 다익스트라
    2. new_cost를 갱신시키면서 적은 경로를 채택하도록 구현
'''
import heapq, sys
input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
problem = 1

while True:
  n = int(input())
  
  if n == 0:
    break

  graph = []
  distance = [[INF for _ in range(n)] for _ in range(n)]
  for i in range(n):
    graph.append(list(map(int, input().split())))

  
  h = []
  distance[0][0] = graph[0][0]
  heapq.heappush(h, (distance[0][0], 0, 0))

  while h:
    cost, x, y = heapq.heappop(h)

    if cost < distance[x][y]: 
      continue
      
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0<= nx < n and 0 <= ny < n:
        new_cost = cost + graph[nx][ny]
        if new_cost < distance[nx][ny]:
          heapq.heappush(h, (new_cost, nx, ny))
          distance[nx][ny] = new_cost

  print("Problem " + str(problem) + ":", end = ' ')
  print(distance[n-1][n-1])
  problem += 1
