'''
    7576 토마토(1)
    알고리즘:
    (구글링하여 참고해서 푼 문제 --> 다시 풀어보기)
    1. 익은 토마토를 찾고, 그 토마토에 대하여 상하좌우를 탐색해서 큐에 넣는다
    2. 이 때, queue의 길이만큼 다 확인하는 만큼이 1일치이다
'''
import sys
from collections import deque
def bfs():
    days = 0
    while q:
        days += 1
        
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if (0<=nx<N) and (0<= ny < M):
                    if tomato[nx][ny] == 0:
                        tomato[nx][ny] = 1
                        q.append([nx, ny])
        
    return days

M, N = map(int, sys.stdin.readline().split())
tomato = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1: # 익은 토마토가 있는 부분에 대해서 queue에 넣기
            q.append([i, j])

result = bfs() -1
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
print(result)