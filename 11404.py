'''
    11404 플로이드
    알고리즘:
    1. 플로이드 알고리즘 사용
    2. 한 도시에서 다른 도시로 가는 노선이 여러개인 경우, 최솟값을 넣어서 최단거리가 될 수 있도록 한다
'''
import sys
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: # 시작 도시와 도착 도시가 같은 경우는 없다는 조건
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c) # 도시로 가는 노선이 여러개라면, 최단거리를 가기 위해서는 최솟값이 들어가야한다
    
# 플로이드 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF: # 갈 수 없는 경우 0 출력
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()