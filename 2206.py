'''
    2206 벽 부수고 이동하기
    (모르겠어서 구글링 한 문제, 아직 이해 잘 못함... --> 다시 풀어볼 것)
    알고리즘:
    1. 벽이 아닌 경우 일반적인 bfs
    2. 벽인 경우 이면서, 벽을 뚫은 적이 없는 경우 세번째 차수 값 수정하여 큐에 삽입
'''
import sys
from collections import deque
def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1 

    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (0<= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 0 and visited[nx][ny][c] == -1:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append([nx, ny, c])
                elif c == 0 and graph[nx][ny] == 1 and visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])

N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
bfs()
ans1 = visited[N-1][M-1][0]
ans2 = visited[N-1][M-1][1]

if ans1 != -1 and ans2 != -1:
    print(min(ans1, ans2))
elif ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(-1)