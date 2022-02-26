'''
    알고리즘:
    1. 최소한의 비용으로 두 집을 왕래한다 -> 크루스칼 알고리즘 생각
    2. 절약할 수 있는 비용을 출력하기 위해서는, '모든 간선의 비용 - 크루스칼 알고리즘 적용한 최소한의 비용' 을 계산
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

while True:
  n, m = map(int, input().split())

  if n == 0 and m == 0:
    break
    
  edges, parent = [], [0] * (n)
  
  for i in range(n):
    parent[i] = i
    
  for i in range(m):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))
  edges.sort(key = lambda x:x[2])
  
  cost, total = 0, 0
  for edge in edges:
    a, b, c = edge
    total += c
    
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
      cost += c
  
  print(total - cost)
