'''
    7562 나이트의 이동
    알고리즘:
    1. 나이트가 갈 수 있는 8방향의 좌표를 정의하고, 최소이동이므로 bfs사용
    2. bfs의 종료 조건 설정할 생각을 못해냈다 --> 큐에서 빼낸 값이 같으면 종료해도된다 
'''
from collections import deque
def bfs(x, y):
    q = deque()
    q.append([x, y])
    chess[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == dox and y == doy:
            return (chess[x][y] - 1)

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if (0<= nx < L) and (0 <= ny < L) and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append([nx, ny])

T = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for i in range(T):
    L = int(input())
    chess = [[0] * L for i in range(L)]

    x, y = map(int, input().split())
    dox, doy = map(int, input().split())
    print(bfs(x, y))
