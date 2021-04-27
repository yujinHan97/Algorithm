'''
    1167 트리의 지름
    알고리즘:
    (구글링한 문제, 나중에 다시 풀어보기)
    1. bfs 알고리즘을 이용
    2. 임의로 1에 대해서 가장 먼 거리에 있는 노드를 구한다
    3. 그러면 그 노드로부터 가장 먼 거리에 있는 노드를 구하면 그게 지름이다
    4. 즉, bfs를 2번 해야한다
'''
from collections import deque
def bfs(start):
    distance, node = 0, 0
    q = deque()
    visited = [False] * (N+1)
    q.append((start, 0))
    visited[start] = True

    while q:
        now, now_dist = q.popleft()

        for i in tree[now]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append((i[0], i[1] + now_dist))

                # 새로운 최장거리가 있다면, node와 distance 갱신
                if distance < i[1] + now_dist:
                    node = i[0]
                    distance = i[1] + now_dist

    return distance, node

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    a = list(map(int, input().split()))
    
    for i in range(1, len(a)-2, 2):
        tree[a[0]].append((a[i], a[i+1]))

# 두 점 x, y에 대해서 x에 대한 최장 거리가 y노드라면, y노드는 지름의 한 부분
# 따라서, y노드에 대한 지름을 구하면 된다
dist, node = bfs(1)
dist, node = bfs(node)
print(dist)
