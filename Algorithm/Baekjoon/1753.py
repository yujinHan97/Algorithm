'''
    1753 최단경로
    알고리즘:
    1. 다익스트라 알고리즘 이용, 우선순위 큐 활용
'''
import sys
import heapq
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dajikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dajikstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])