'''
    알고리즘:
    1. 일반인과 적록색약을 위한 그림을 따로 두고, dfs시행
    2. 적록색약을 위한 그림은 R을 G로 바꿔서 dfs 한다
'''
import sys
sys.setrecursionlimit(100000)
def dfs(arr, x, y, color):
    arr[x][y] = 'X'
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if (0<= nx < N) and (0<= ny <N) and arr[nx][ny] != 'X':
            if arr[nx][ny] == color:
                dfs(arr, nx, ny, arr[nx][ny])

N = int(input())
pic = [] # 정상인을 위한 그림
piccopy = [] # 적록색약을 위한 그림
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    pic.append(list(map(str, sys.stdin.readline().strip())))
    
# 정상인이 보는 그림을 일단 적록색약이 보는 그림에 복사
piccopy = [[]* N for i in range(N)]
for i in range(N):
    for j in range(N):
        piccopy[i].append(pic[i][j])
        
# 적록색맹은 R과 G를 구분 못하므로, R을 G로 바꿈
for i in range(N):
    for j in range(N):
        if piccopy[i][j] == 'R':
            piccopy[i][j] = 'G'

result1 = result2 = 0
for i in range(N):
    for j in range(N):
        if pic[i][j] == 'R' or pic[i][j] == 'G' or pic[i][j] == 'B':
            color = pic[i][j]
            dfs(pic, i, j, color)
            result1 += 1
        if piccopy[i][j] == 'G' or piccopy[i][j] == 'B':
            color = piccopy[i][j]
            dfs(piccopy, i, j, color)
            result2 += 1

print(result1, end = ' ')
print(result2)
