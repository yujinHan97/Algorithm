'''
    알고리즘:
    1. 선수과목 간선을 그래프와 진입차수 리스트에 추가하면서 기록
    2. 위상정렬 수행
    3. 연결된 그래프마다 진입차수도 한번씩 빼고, 학기 수는 증가
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ins = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  ins[b] += 1

q = deque()
result = [0] * (n+1)
for i in range(1, n+1):
  if ins[i] == 0:
    q.append(i)
    result[i] = 1

while q:
  now = q.popleft()
  for new_node in graph[now]:
    ins[new_node] -= 1
    # 차수를 줄일 때 마다 학기수는 1씩 증가
    result[new_node] = result[now] + 1
    if ins[new_node] == 0:
      q.append(new_node)

print(*result[1:])
