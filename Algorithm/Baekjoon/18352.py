'''
    18352 특정 거리의 도시 찾기
    알고리즘:
    1. 최단거리이므로, bfs 진행
    2. 이미 갔던 길은 확인하지 않는다. 
    3. 가보지 않았던 길을 모두 확인하고, 나중에 K와 같은 값을 갖는 도시 찾기
'''
import sys
from collections import deque
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        node = q.popleft()
        
        for x in graph[node]:
            if visited[x] == False: # 안 가본 곳에 대해서만 경로 Update (이미 가본 곳이면 최단 경로가 아니니까)
                visited[x] = True
                q.append(x)
                c[x] = c[node] + 1

N, M, K, X = map(int, sys.stdin.readline().split())

# 양방향 연결이 아니라 단방향 연결이니까 그냥 행렬이 아닌 리스트로 표현
graph = [[] for i in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    
visited = [False] * (N+1)
c = [0] * (N+1)
bfs(X)

# bfs 다 완료 후, 최단 경로 중에 K와 같은 값 찾기
city = []
for i in range(1, N+1):
    if c[i] == K:
        city.append(i)

if len(city) == 0:
    print(-1)
else:
    for i in city:
        print(i)