'''
    알고리즘:
    1. 여행지 노드가 같은 집합에 속하면 => 여행 가능
    2. 여행지 노드 사이에 도로가 존재하면 union
    3. 여행 가능 경로를 검사하면 되는데, 첫번째 여행지를 기준으로 해서 그 여행지와 모두 같은 집합인지 find
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
    
  return parent[x]
  
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a >= b:
    parent[a] = b
  else:
    parent[b] = a
    
n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
  
for i in range(n):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 1:
      union_parent(parent, i+1, j+1)

travel = list(map(int, input().split()))
root = find_parent(parent, travel[0])
poss = True
for i in range(1, len(travel)):
  if root != find_parent(parent, travel[i]):
    poss = False
    break

if poss:
  print("YES")
else:
  print("NO")
