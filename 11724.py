'''
    11724 연결요소의 개수
    알고리즘:
    1. 방문하지 않은 것들에 대해서 bfs를 하고, 그 횟수를 센다 
    2. bfs를 하면서 인접한 것들은 방문 처리를 하므로, 연결 요소의 개수를 알 수 있다
'''
import sys
from collections import deque
def dfs(x):
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        for node in graph[x]:
            if visited[node] == 0:
                visited[node] = 1
                q.append(node)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
result = 0
q = deque()

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)