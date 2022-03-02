'''
    알고리즘:
    1. 서로 연결된 컴퓨터들을 그룹화, 서로 다른 그룹의 개수 찾기? => 서로소 집합 떠올림
    2. 서로소 집합이므로 union-find 알고리즘 구현
    3. 마지막으로, find함수 한 번씩 호출하면서 경로 최적화하기!
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, computers):
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
        
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent, i+1, j+1)
    
    # find 함수를 한 번씩 호출하면서, 경로 최적화하기 => 이것 때문에 TC 1개 계속 틀렸음.
    for i in range(1, n+1):
        find_parent(parent, i)
    
    return len(set(parent[1:]))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    알고리즘:
    1. BFS 이용해서, 방문하지 않았던 곳에서 연결된 곳은 모두 방문 처리
    2. bfs 호출할 때마다 연결된 네트워크가 있다는 의미
'''
from collections import deque
def bfs(node, graph, visited):
    q = deque([node])
    visited[node] = True
    
    while q:
        now = q.popleft()
        for new_node in graph[now]:
            if visited[new_node] == False:
                visited[new_node] = True
                q.append(new_node)
                
def solution(n, computers):
    visited = [False] * (n+1)
    graph = [[] * (n+1) for i in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
                
            if computers[i][j] == 1:
                graph[i+1].append(j+1)

    count = 0
    for i in range(1, n+1):
        # print(visited)
        if visited[i] == False:
            bfs(i, graph, visited)
            count += 1
        
    return count
    
