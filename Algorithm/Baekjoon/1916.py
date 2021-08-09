'''
    1916 최소비용 구하기
    알고리즘:
    1. 다익스트라 알고리즘 활용
'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())

def dajik(start):
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

dajik(start)
print(distance[end]) # start로 시작해서 end로 가는 최단경로를 구하는 것
