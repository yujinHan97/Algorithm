'''
    알고리즘:
    (원래 내 풀이는 모든 노드끼리의 거리 정렬 -> 시간초과)
    1. 한 노드에서 다른 모든 노드와의 거리를 구하지 않고 한 노드와 가장 가까운 노드만을 찾는다
    2. x, y, z 를 위와 같은 방법으로 계산하고 정렬 후, 크루스칼 알고리즘 수행
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

  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
n = int(input())
edges = []
parent = [0] * n

x, y, z = [], [], []
for i in range(n):
  parent[i] = i
  x_, y_, z_ = map(int, input().split())
  x.append((x_, i))
  y.append((y_, i))
  z.append((z_, i))
x.sort()
y.sort()
z.sort()

# 인접한 노드와의 거리, 어떤 2개의 노드인지에 대한 정보를 edges에 저장 
# (가중치, 행성a, 행성b)
for i in range(n-1):
  edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
  edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
  edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
edges.sort()

min_cost = 0
for edge in edges:
  c, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    min_cost += c

print(min_cost)
