'''
    1780 종이의 개수   
    알고리즘:
    (색종이 만들기와 똑같은 문제)
    1. 매개변수로 들어오는 수를 나머지 수와 같은지 확인하는데, 다르다면 그 구역을 9분할
    2. 수가 같아질 때까지 재귀호출하며 분할, 수가 같아진다면 개수 세기
'''
import sys

def sol(x, y, N):
    num = paper[x][y]
    global pos_one, zero, neg_one

    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != paper[i][j]:
                sol(x, y, N//3)
                sol(x, y + N//3, N//3)
                sol(x, y + (N//3)*2, N//3)
                sol(x+ N//3, y, N//3)
                sol(x+ N//3, y + N//3, N//3)
                sol(x+ N//3, y + (N//3)*2, N//3)
                sol(x+ (N//3)*2, y, N//3)
                sol(x+ (N//3)*2, y+ N//3, N//3)
                sol(x+ (N//3)*2, y+ (N//3)*2, N//3)
                return 

    if num == 0:
        zero += 1
    elif num == -1:
        neg_one += 1
    elif num == 1:
        pos_one += 1

N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

neg_one = zero = pos_one = 0
sol(0, 0, N)