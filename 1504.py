'''
    1504 특정한 최단 경로
    알고리즘:
    (거쳐서 가야 한다길래, 플로이드로 풀었지만 시간초과 --> 구글링했으므로 다시 풀기)
    1. 1 --> V1 --> V2 --> N 의 방법과
       1 --> V2 --> V1 --> N 의 방법이 있다. 
    2. 총 3번의 다익스트라 호출을 한 후의 최솟값을 찾는다
    3. result1 = dajik(1)한 dist[v1] + dajik(v1)한 dist[v2] + dajik(v2)한 dist[N]
       result2 = dajik(1)한 dist[v2] + dajik(v2)한 dist[v1] + dajik(v1)한 dist[N]
       의 최솟값이며, 그 값이 INF이상이면 도달할 수 없는 경로
'''
import sys
import heapq

def dajikstra(start):
    q = []
    dist = [INF] * (N+1) # 다익스트라를 여러번 부를거니까 
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, now = heapq.heappop(q)

        if d > dist[now]:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist # 최단 경로 테이블 반환

INF = int(1e9)
N, E = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

from_1 = dajikstra(1) # 1을 시작으로 한 다익스트라 최단경로 테이블 
from_v1 = dajikstra(v1) # v1을 시작으로 한 다익스트라 최단경로 테이블
from_v2 = dajikstra(v2) # v2를 시작으로 한 다익스트라 최단경로 테이블

result1 = from_1[v1] + from_v1[v2] + from_v2[N]
result2 = from_1[v2] + from_v2[v1] + from_v1[N]

total = min(result1, result2)

if total >= INF:
    print(-1)
else:
    print(total)
