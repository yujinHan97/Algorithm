import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  rank = list(map(int, input().split()))
  ins = [0] * (n+1)
  graph = [[] for _ in range(n+1)]
  
  for i in range(n):
    graph[rank[i]] = rank[i+1:]
    ins[rank[i]] = i
    
  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    if b in graph[a]:
      graph[b].append(a)
      graph[a].remove(b)
      ins[a] += 1
      ins[b] -= 1
    else:
      graph[a].append(b)
      graph[b].remove(a)
      ins[a] -= 1
      ins[b] += 1
      
  q = deque()
  for i in range(1, n+1):
    if ins[i] == 0:
      q.append(i)
      
  result = []
  while q:
    node = q.popleft()
    result.append(node)
    
    for new_node in graph[node]:
      ins[new_node] -= 1
      if ins[new_node] == 0:
        q.append(new_node)

  if len(result) == n:
    print(*result)
  else:
    print("IMPOSSIBLE")
