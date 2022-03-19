'''
    알고리즘:
    1. 모든 컴퓨터를 최소 비용으로 연결 -> 최소 스패닝 트리 알고리즘 구현
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
    
n = int(input())
m = int(input())
edges = []

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
  
for i in range(m):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))
edges.sort(key = lambda x:x[2])

result = 0
for edge in edges:
  a, b, cost = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
