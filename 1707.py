'''
    알고리즘: 
    (구글링 해서 풀었으니까 나중에 다시 풀 것)
    1. 인접한 노드에 대해서는 다르게 표시
    2. 만약 인접한 노드인데 숫자가 같게 표시가 되어있다면, 이분 그래프가 아닌것
'''    
import sys
from collections import deque
def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        x = q.popleft()
        for adj in graph[x]: 
            if visited[adj] == 0: # 인접한 노드인데 아직 안 가본 노드라면, 나와는 다른 번호로 표기
                visited[adj] = -visited[x]
                q.append(adj)
            else:
                if visited[adj] == visited[x]: # 인접한 노드인데 같은 번호가 적혀있다면, 이분 그래프가 아니다
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V+1)
    flag = 1
    for i in range(1, V+1):
        if visited[i] == 0:
            if bfs(i) == False: # 이분 그래프가 아닌 경우 중단
                flag = -1
                break

    if flag == -1:
        print("NO")
    else:
        print("YES")
