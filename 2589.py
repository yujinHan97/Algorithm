'''
    2589 보물섬
    알고리즘:
    (구글링 해본 문제 --> 다시 풀어볼 것)
    1. 보물이 어디 있는지 모르니까 일단 L인 모든 칸에대해서 bfs를 수행
    2. bfs를 수행했을 때, 가장 멀리 있는 곳을 해당 칸에서의 보물까지의 거리니까 그거를 저장
    3. 마지막에 그 중 최댓값을 고른다
'''
import sys
from collections import deque
def bfs(x, y):
    q = deque()
    visited = [[0] * M for i in range(N)] # 보물까지의 거리를 저장할 visited
    q.append([x, y])
    visited[x][y] = 1
    result = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (0<= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny]) - 1 
                    q.append([nx, ny])

    return result

N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))

print(cnt)