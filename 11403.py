'''
    알고리즘:
    1. 모든 정점에 대해서 BFS 수행
    2. BFS 수행 완료 후, 각 정점에서 갈 수 있는 것들 (TRUE)인 애들만 1로 처리
    (다른 풀이 보니 플로이드 워셜도 있음 -> O(n^3)이라 BFS가 나을수도)
'''
from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
  arr = list(map(int, input().split()))
  for j in range(len(arr)):
    if arr[j] == 1:
      graph[i].append(j)

def bfs(node, graph, visited):
  q = deque([node])

  while q:
    i = q.popleft()
    for newNode in graph[i]:
      if visited[newNode] == False:
        q.append(newNode)
        visited[newNode] = True
        
output = []
for i in range(N):
  visited = [False] * N
  bfs(i, graph, visited)

  temp = []
  for j in range(N):
    if visited[j] == True:
      temp.append(1)
    else:
      temp.append(0)
      
  output.append(temp)

for i in range(N):
  for j in range(N):
    print(output[i][j], end = ' ')
  print()
