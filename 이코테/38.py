'''
    알고리즘:
    (오래 걸렸지만, 해설 보지 않고 풀이 생각해냈다)
    (근데 이게 최단경로 문제인지 잘 모르겠음. 만약 그냥 시험에 나왔다면 최단경로로 풀 생각을 못했을 것 같다)
    1. 각 노드마다, 다른 노드에 도달 가능한지 체크한다 (다른 노드에서도 해당 노드가 도달 가능한지도 체크)
    2. 도달이 불가능하다면, 순위를 알 수 없는 것. 
'''
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
      
  if count == n:
    result += 1
print(result)
