'''
    알고리즘:
    (모든 비용이 1이므로, BFS 사용 가능)
    1. 1번 노드에서부터 다른 모든 노드 까지의 최단 거리를 구하고, 그 최단 거리가 가장 긴 노드를 찾는 문제
    2. 다익스트라로, 매번 cost를 +1 하면서 dist 갱신
'''
import heapq

n, m = map(int, input().split())
INF = int(1e9)
hide = [[] for i in range(n+1)]
dist = [INF] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  hide[a].append(b)
  hide[b].append(a)

q = []
heapq.heappush(q, (0, 1))
dist[1] = 0

while q:
  cost, start = heapq.heappop(q)
  
  if dist[start] < cost:
    continue
  for node in hide[start]:
    new_cost = cost + 1
    if new_cost < dist[node]:
      heapq.heappush(q, (cost+1, node))
      dist[node] = cost + 1

hide_num, max_dist = 0, 0
for i in range(1, n+1):
  if max_dist < dist[i]:
    max_dist = dist[i]
    hide_num = i

print(hide_num, end = ' ')
print(max_dist, end = ' ')
print(dist.count(max_dist))
