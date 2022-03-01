'''
    알고리즘:
    1. 일부 학생들의 순서가 있고, 이들을 정렬 -> 위상정렬
    2. 진입차수가 0이 될 때마다 result 리스트에 추가하면 그게 키 순서이다. 
'''
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ins = [0] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  ins[b] += 1

q = deque()
for i in range(1, n+1):
  if ins[i] == 0:
    q.append(i)

result = []
while q:
  now = q.popleft()
  result.append(now)

  for new_node in graph[now]:
    ins[new_node] -= 1
    if ins[new_node] == 0:
      q.append(new_node)

print(*result)
