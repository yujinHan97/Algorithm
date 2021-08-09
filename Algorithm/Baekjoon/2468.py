'''
    2468 안전영역
    알고리즘:
    1. 장마의 양을 0부터 지역의 최대 높이까지 설정해 가면서 잠기는 곳과 잠기지 않는 곳을 구분
    2. 각 높이에 대하여 dfs 수행하고, 잠기지 않는 영역의 수를 구한다
    3. 잠기지 않는 영역의 수를 모두 저장하고, 그 중 max를 출력
'''
import sys
sys.setrecursionlimit(100000)
def dfs(x, y):
    c[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if (0<= nx < N) and (0 <= ny < N):
            if c[nx][ny] == 0:
                dfs(nx, ny)

N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
maxh = max(map(max, graph)) # 지역에서 가장 높은 높이 지역의 높이 찾기

countings = []
for h in range(maxh + 1): # 모든 높이에 대해서 검사
    c = [[0] * N for _ in range(N)] # 잠긴 곳과 잠기지 않은 곳을 표기할 배열

    for i in range(N):
        for j in range(N):
            if graph[i][j] <= h:
                c[i][j] = 1 # 잠긴 곳은 1로 표시

    result = 0
    for i in range(N):
        for j in range(N):
            if c[i][j] == 0: # 잠기지 않은 곳이니까 그 곳에 대하여 dfs
                dfs(i, j)
                result += 1

    countings.append(result)

print(max(countings))