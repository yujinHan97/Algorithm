'''
    2583 영역 구하기 
    알고리즘:
    1. 0으로 초기화된 모눈종이를 놓고, 직사각형에 해당하는 좌표에다 1로 표기
    2. dfs 수행해서 영역의 개수 구하기
    (문제에서 인덱스가 배열과 다르게 나와있어서 뒤집느라 조금 힘들었다)
'''
import sys
sys.setrecursionlimit(100000)
def dfs(x, y):
    graph[x][y] = 1
    global count 
    count += 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if (0<= nx < M) and (0<= ny < N):
            if graph[nx][ny] == 0:
                dfs(nx, ny)

M, N, K = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0] * N for _ in range(M)]
coord = []
for i in range(K):
    coord.append(list(map(int, sys.stdin.readline().split())))

# 입력된 좌표로 모눈종이에 직사각형의 면적에 해당하는 부분을 1로 만든다
for i in coord:
    col = i[2] - i[0]
    row = i[3] - i[1]

    for x in range(row):
        for y in range(col):
            graph[M-i[3] + x][i[0] + y] = 1

result = 0
countings = []
for i in range(M):
    for j in range(N):
        count = 0
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1
            countings.append(count)

print(result)
countings.sort()
for i in countings:
    print(i, end = ' ')