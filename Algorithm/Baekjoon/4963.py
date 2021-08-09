'''
    4963 섬의 개수
    알고리즘:
    1. 대각선까지 고려해야 하므로, 총 8가지의 경우의 수 고려
    2. 그 외에는 같은 dfs 알고리즘이다
'''
import sys
sys.setrecursionlimit(10000)
def dfs(x, y):    
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if (0<= nx < h) and (0<= ny < w):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)

while True:
    w, h= map(int, sys.stdin.readline().split())
    if w == 0 and h ==0 :
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] > 0:
                dfs(i, j)
                result += 1

    print(result)