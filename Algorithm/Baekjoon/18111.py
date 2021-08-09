'''
    18111 마인크래프트
    --> pypy로 돌렸다...
    --> 처음에는 매번 block에서 빼고 block에 더하고 시간도 그렇게 했는데 한번에 plus, minus로 계산해서 시간초과 벗어남
    알고리즘:
    1. 모든 높이에 대해서 완전탐색
    2. 높이를 고르게 하기 위해서 빼야할 블럭과 쌓아야할 블럭의 개수 구한 후, 시간도 측정    
'''
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
answer = []
for h in range(257):
    plus, minus = 0, 0
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] > h:
                plus += (ground[i][j] - h)
            else:
                minus += (h - ground[i][j]) 
    
    block = B + plus
    if block < minus:
        continue
    
    time = plus * 2 + minus
    answer.append((time, h))

answer.sort(key = lambda x:(x[0], -x[1]))
print(answer[0][0], answer[0][1])    
