'''
    알고리즘:
    1. 모든 행성을 연결하고, 비용을 최소로? => 크루스칼 알고리즘
    2. 메모리 제한을 만족시키기 x, y, z로 나눠서 정렬하고 각각의 거리 차이만 저장
    3. 그 후, 크루스칼 알고리즘 수행
'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
  
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a <= b:
    parent[b] = a
  else:
    parent[a] = b
    
n = int(input())
xs, ys, zs = [], [], []
parent = [i for i in range(n)]

for i in range(n):
  x, y, z = map(int, input().split())
  xs.append([x, i])
  ys.append([y, i])
  zs.append([z, i])

xs.sort(key = lambda x:x[0])
ys.sort(key = lambda x:x[0])
zs.sort(key = lambda x:x[0])

edges = []
for i in range(n-1):
  edges.append((xs[i+1][0] - xs[i][0], xs[i][1], xs[i+1][1]))
  edges.append((ys[i+1][0] - ys[i][0], ys[i][1], ys[i+1][1]))
  edges.append((zs[i+1][0] - zs[i][0], zs[i][1], zs[i+1][1]))
edges.sort()

cost = 0
for edge in edges:
  if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
    union_parent(parent, edge[1], edge[2])
    cost += edge[0]
    
print(cost)
