'''
    알고리즘:
    (그림 참고 : https://soobarkbar.tistory.com/181)
    1. 각 게이트의 루트가 0이 아니라면, 현재 게이트 이하의 번호에서 도킹할 수 있는 게이트가 있다는 의미
    2. 현재 도킹할 수 있는 게이트가 있다면, 현재 입력된 번호 게이트가 속한 루트를 찾고 루트의 왼쪽 게이트와 union연산 수행
    3. 반복하면, 결국 현재 게이트 이하의 게이트에서 도킹할 곳이 없을 경우, 루트는 0을 반환할 것
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
    
g = int(input())
p = int(input())
parent = [0] * (g+1)

for i in range(1, g+1):
  parent[i] = i
  
result = 0
for i in range(p):
  gi = int(input())

  temp = find_parent(parent, gi)
  if temp == 0:
    break

  union_parent(parent, temp-1, temp)
  result += 1
    
print(result)
