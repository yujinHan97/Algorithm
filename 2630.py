'''
    2630 색종이 만들기   
    알고리즘:
    (정답률이 70%가 넘는데도 구글링을 해서 풀었다.. 나중에 다시 풀기!)
    1. 첫 색상이 나머지 색상과 같은지 확인하는데, 다르다면 그 구역을 4분할
    2. 색상이 같아질 때까지 재귀호출하며 분할, 색상이 같아진다면 개수 세기
'''
import sys
def sol(x, y, N):
    color = paper[x][y]
    global white, blue

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]: # 색이 다르다면 4분할
                sol(x, y, N//2) # 2사분면
                sol(x, y+N//2, N//2) # 1사분면
                sol(x+N//2, y, N//2) # 3사분면
                sol(x+N//2, y+N//2, N//2) # 4사분면
                return

    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = []
white = blue = 0
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

sol(0, 0, N)
print(white)
print(blue)