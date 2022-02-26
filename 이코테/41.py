'''
    알고리즘:
    1. 여행계획에 속해 있는 노드들이 모두 같은 그룹게 속하면 여행 가능한 것임을 생각
    2. 따라서, 주어진 모든 간선 정보를 이용해서 union 연산을 수행
    3. 첫번째 계획을 기반으로, 다른 계획들도 첫번째 계획과 같은 부모를 가진다면 계속하고 다른 부모를 가진다면 중단하여 NO 출력
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
m = int(input())
graph = [[] for i in range(n+1)]
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
  
for i in range(n):
  arr = list(map(int, input().split()))
  for j in range(len(arr)):
    if arr[j] == 1:
      union_parent(parent, i+1, j+1)
plans = list(map(int, input().split()))

trip = True
start = parent[plans[0]]
for plan in plans:
  if start == parent[plan]:
    continue
  else:
    trip = False
    break

if trip:
  print("YES")
else:
  print("NO")
