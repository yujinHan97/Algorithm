'''
    알고리즘:
    1. 최단 거리를 찾기 위해서 BFS를 사용
    2. distance를 INF로 초기화해놓고, q에서 뺀 노드에다가 한 번 더 간 만큼 distance 갱신
'''
from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
  q = deque([start])
  distance[start] = 0

  while q:
    node = q.popleft()

    for i in graph[node]:
      if distance[i] == INF:
        q.append(i)
        distance[i] = distance[node] + 1

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)

bfs(X)

isExist = False
for i in range(1, N+1):
  if distance[i] == K:
    isExist = True
    print(i)

if not isExist:
  print(-1)
