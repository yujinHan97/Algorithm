'''
    알고리즘:
    1. 최소 스패닝 트리를 만들기 위해서, edge의 비용 순으로 정렬
    2. 정렬 후, 모든 edge에 대해서 cycle이 존재하지 않으면 union연산 수행하고 cost를 더한다
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
    
v, e = map(int, input().split())
edges = []

parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i
  
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))
edges.sort(key=lambda x:x[2])

result = 0
for edge in edges:
  a, b, cost = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
print(result)
