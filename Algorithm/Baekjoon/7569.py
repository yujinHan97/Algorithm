'''
    7569 토마토(2)
    알고리즘:
    1. 토마토(1)과 같은 문제인데, 위 아래만 추가되었다
    2. 위, 아래에 대해서 z값을 움직일 수 있는 방법을 추가하고 같은 방법으로 풀면 된다
'''
import sys
from collections import deque
def bfs():
    days = 0
    while q:
        days += 1
        for _ in range(len(q)):
            z, x, y = q.popleft()
            for i in range(6):
                nx = dx[i] + x
                ny = dy[i] + y
                nz = dz[i] + z

                if (0<= nx < N) and (0<= ny < M) and (0<= nz < H):
                    if tomato[nz][nx][ny] == 0:
                        tomato[nz][nx][ny] = tomato[z][x][y] +1
                        q.append([nz, nx, ny])

    return days-1

M, N, H = map(int, input().split())
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
tomato = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])

result = bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
print(result)