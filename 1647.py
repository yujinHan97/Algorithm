'''
    알고리즘:
    1. 무방향 그래프의 유지비를 최소 비용으로 하고 싶다? -> 크루스칼 알고리즘 생각 (여기까지 잘 생각했다)
    2. 마을을 2개로 나누고 싶다면? -> 크루스칼 알고리즘을 하고, 가장 큰 유지비가 드는 간선을 제거하면, 2개의 그룹이 생김 (여기는 책을 보고 알았음)
    3. last를 선언해서 가장 긴 간선을 제거할 것. (edges를 정렬했으니까 마지막 간선이 가장 큰 유지비가 드는 간선이기 때문에)
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

N, M = map(int, input().split())

edges = []
parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

for _ in range(M):
  A, B, C = map(int, input().split())
  edges.append((C, A, B))

edges.sort()

result, last = 0, 0
for i in range(M):
  a = edges[i][1]
  b = edges[i][2]
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += edges[i][0]
    last = edges[i][0]

print(result-last)
