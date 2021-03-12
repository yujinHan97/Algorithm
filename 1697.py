'''
    1697 숨바꼭질
    알고리즘:
    1. 최단 경로니까 bfs이용
    2. 갈 수 있는 방향은 -1, +1, *2로 갈 수 있는 경우에 queue에 삽입
'''
from collections import deque
def bfs(a):
    q = deque([a])

    while q:
        x = q.popleft()

        if x == K:
            print(c[x])
            break

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < 100001 and c[nx] == 0:
                c[nx] = c[x] + 1
                q.append(nx)
    
N, K = map(int, input().split())
c = [0] * 100001

bfs(N)