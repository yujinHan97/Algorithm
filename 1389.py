'''
    알고리즘:
    1. 연결된 친구들을 인접리스트 형식으로 저장
    2. 모든 사람에 대하여 각각 BFS 사용해서 인접한 친구들의 최소 거리를 구하여 케빈 베이컨 수를 구함
'''
from collections import deque
def bfs(person):  
  q = deque([person])
  levels[person] = 0
  sum_level = 0

  while q:
    node = q.popleft()
    for nNode in friends[node]:
      if levels[nNode] == -1:
        levels[nNode] = levels[node] + 1
        q.append(nNode)

  for i in range(1, n+1):
    if levels[i] != -1:
      sum_level += levels[i]

  return sum_level

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

level = []
for i in range(1, n+1):
  levels = [-1] * (n+1)
  dist = bfs(i)
  if dist != 0:
    level.append((dist, i))
    
level.sort(key = lambda x:(x[0], x[1]))
print(level[0][1])
