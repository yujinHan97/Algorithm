'''
    알고리즘:
    1. 순위에 맞추어 정렬 => 위상정렬
    2. 위상 정렬의 특이 케이스는 2가지
       - 사이클 발생 => q의 len이 0 인지 검사
       - 결과가 1개가 아니라 여러개 => q의 len이 2 이상인지 검사
    3. 그 외는 모두 위상 정렬 답은 정확히 1개
    4. 등수를 그래프로 생각하고 순위가 바뀌면 진입차수 -1, +1로 조작해서 구현
'''
from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  n = int(input())
  last = list(map(int, input().split()))
  graph = [[] for _ in range(n+1)]
  indegree = [0] * (n+1)
  
  for i in range(n-1):
    for j in range(i+1, n):
      graph[last[i]].append(last[j])
      indegree[last[j]] += 1

  ch = int(input())
  for i in range(ch):
    a, b = map(int, input().split())

    if b in graph[a]:
      graph[a].remove(b)
      graph[b].append(a)
      indegree[a] += 1
      indegree[b] -= 1
    elif a in graph[b]:
      graph[b].remove(a)
      graph[a].append(b)
      indegree[a] -= 1
      indegree[b] += 1

  result = []
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)

  questionmark = False
  cycle = False
  for i in range(n):
    if len(q) == 0:
      cycle = True
      break
    if len(q) >= 2:
      questionmark = True
      break
      
    now = q.popleft()
    result.append(now)
    for node in graph[now]:
      indegree[node] -= 1

      if indegree[node] == 0:
        q.append(node)

  if questionmark:
    print("?")
  elif cycle:
    print("IMPOSSIBLE")
  else:
    print(*result)
