'''
    1260 DFS와 BFS
    알고리즘:
    1. DFS, BFS의 개념을 알면 풀 수 있다 
'''
import sys
from collections import deque
def dfs(graph, v, visiteddfs):
    visiteddfs[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if visiteddfs[i] == False:
            dfs(graph, i, visiteddfs)

def bfs(graph, v, visitedbfs):
    q = deque([v])
    visitedbfs[v] = True
    
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visitedbfs[i] == False:
                q.append(i)
                visitedbfs[i] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1): # 방문할 정점이 여러개일 때 작은 번호 먼저 가기 위해서 정렬
    graph[i].sort()

visiteddfs = [False] * (N+1)
dfs(graph, V, visiteddfs)
print()
visitedbfs = [False]* (N+1)
bfs(graph, V, visitedbfs)