'''
    알고리즘:
    (BFS로 푸는지 감도 못잡아서 구글링을 했다)
    1. 입력된 연결을 이용해서 tree 연결을 graph처럼 만든다
    2. 각 노드마다 bfs를 하면서, 부모를 지정해준다
'''
import sys 
from collections import deque

input = sys.stdin.readline
N = int(input())
tree = [[] for i in range(N+1)]
parents = [0] * (N+1)
visited = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS 시작
q = deque([1])
visited[1] = True

while q:
    v = q.popleft()

    for i in tree[v]:
        if visited[i] == False:
            parents[i] = v # 부모 설정
            q.append(i)
            visited[i] = True
            
for i in range(2, N+1):
    print(parents[i])
