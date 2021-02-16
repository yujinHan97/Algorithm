'''
    2606 바이러스
    알고리즘:
    1. 각 컴퓨터들이 연결되도록 adj에 연결 점을 생성
    2. 첫번째 점에서 dfs를 실시하고, dfs로 가면 visited 리스트가 변한다
    3. visited가 True라는 건, 1에서 어떻게든 연결되어있단 의미이므로, 
    4. 1번을 제외한 visited가 True의 개수를 구하면 감연된 컴퓨터의 개수
'''
def dfs(adj, start, visited):
    visited[start] = True

    for x in adj[start]:
        if visited[x] == False:
            dfs(adj, x, visited)

n = int(input())
conn = int(input())
count = 0

net = []
for _ in range(conn):
    net.append(list(map(int, input().split())))

# net을 이용하여, 어떤 점에 어떤 점이 연결되어 있는지 리스트 생성
adj = [[] for _ in range(n+1)]
for x in net:
    adj[x[0]].append(x[1])
    adj[x[1]].append(x[0])

# 모든 점들을 False로 초기화하고, 1번 컴퓨터부터 dfs시작
visited = [False] * (n+1)
dfs(adj, 1, visited)

for i in range(2, n+1): 
    if visited[i] == True:
        count += 1
print(count)