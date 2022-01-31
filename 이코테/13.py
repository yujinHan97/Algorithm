'''
    알고리즘:
    1. 치킨집 m개의 조합을 구해서 모든 치킨집과 모든 집과의 거리를 구한다
    2. 그 중 가장 짧은 거리를 구하면 답
'''
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

store = []
for i in range(n):
  for j in range(n):
    if city[i][j] == 2:
      store.append((i, j))

# 치킨 가게들 중에서 m개의 치킨 집을 고르는 작업
chick_list = combinations(store, m)
length = []
# 모든 가능한 치킨집 조합 중 하나씩 검사
for chick in chick_list:
  total = 0
  for i in range(n):
    for j in range(n):
      if city[i][j] == 1: # 집이라면, 
        dist = int(1e9)
        for x in chick: # 조합에는 여러 치킨 집에 있는데 가장 가까운 치킨집을 찾는 것 
          temp = abs(x[0]- i) + abs(x[1] - j)
          dist = min(dist, temp)
      
        total += dist
  length.append(total) # 각 조합들에 최종 도시거리를 넣고, 가장 짧은 도시 거리 출력

print(min(length))
