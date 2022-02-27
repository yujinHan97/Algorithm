'''
    알고리즘 : 
    1. 최단거리로 가장 먼 노드를 찾기 위해서, BFS 수행
    2. BFS를 수행하여 가장 먼 거리에 있는 노드를 찾고, 그 거리와 같은 수의 노드가 몇 개인지 찾는다.
'''
from collections import deque

def solution(n, edge):
    INF = int(1e9)
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS 수행
    q = deque([1])
    distance[1] = 0
    
    while q:
        node = q.popleft()
        
        for new_node in graph[node]:
            if distance[new_node] == INF:
                dist = distance[node] + 1
                distance[new_node] = dist
                q.append((new_node))

    # BFS 완료 후 distance에서 가장 큰 거리를 찾고, 가장 큰 거리와 같은 값이 몇 개 있는지 찾기 
    max_dist = max(distance[1:])
    answer = distance.count(max_dist)
    
    return answer
