'''
    2178 미로 탐색
    알고리즘:
    1. 모든 좌표에 대해서 상,하,좌,우 를 탐색하고 갈 수 있다면 +1
    2. 최종적으로 1을 따라서 간 경로가 최단경로
'''
import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])

    return graph[n-1][m-1]   

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))