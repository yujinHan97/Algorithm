'''
    알고리즘: 
    1. 시간초과하지 않기 위해서, 무게 별로 몇 개씩 있는지 저장
    2. A가 낮은 무게부터 고른다고 할 가정 할 때, B가 고를 수 있는 가짓수를 더하면 된다 
'''
n, m = map(int, input().split())
weights = list(map(int, input().split()))

balls = [0] * (m+1)
for i in range(n):
  w = weights[i]
  balls[w] += 1

total = 0
# balls[i] = A가 고를 수 있는 가지 수
# n = B가 고를 수 있는 가지 수 
for i in range(1, m+1):
  n -= balls[i] 
  total += balls[i] * n

print(total)
