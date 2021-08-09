'''
    1012 유기농 배추
    알고리즘:
    1. 1로 되어있는 곳에만 지렁이 있으면 되니까, 1인 곳에 대해서 dfs
    2. 덩어리의 개수를 찾으면 된다
'''
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if (0 <= nx <N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)
        
T = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for i in range(N)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0
    for a in range(N):
        for b in range(M):
            if graph[a][b] > 0:
                dfs(a, b)
                result += 1

    print(result)