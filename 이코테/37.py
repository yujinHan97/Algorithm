'''
    알고리즘:
    1. 같은 경로로 여러가지 길이 있는데, 가장 짧은 경로를 가야하기 때문에 min값을 저장
    2. 플로이드 최단경로 알고리즘을 사용하하여 모든 지점에서 다른 지점으로 가는 최단 경로를 저장하여 구현
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0
      
for i in range(m):
  a, b, cost = map(int, input().split())
  graph[a][b] = min(graph[a][b], cost)
  
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print(0, end = ' ')
    else:
      print(graph[i][j], end = ' ')
  print()
