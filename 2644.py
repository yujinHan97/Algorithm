'''
    2644 촌수계산
    알고리즘:
    1. 정점을 bfs로 해서 연결되어 있다면 그 거리를 출력
    2. 연결되어 있지 않다면 -1을 출력
'''
import sys
from collections import deque
def bfs(start, end):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        visit[node] = 1
        
        if node == end:
            return c[node]

        for x in family[node]:
            if visit[x] == 0:
                c[x] = c[node] + 1
                q.append(x)

n = int(input())
family = [[] for _ in range(n+1)]
a, b = map(int, sys.stdin.readline().split()) 

m = int(input()) 
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

c = [0] * (n+1)
visit = [0] * (n+1)

result = bfs(a, b)
if result == None:
    print(-1)
else:
    print(result)