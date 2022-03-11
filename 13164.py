'''
    알고리즘:
    1. 인접한 유치원생들끼리 그룹을 만들고 최소 비용을 하기 위해서는, 어떤 부분에서 유치원생들의 키 차이가 많이 나는지 찾으면 된다.
    2. 따라서, 인접한 유치원생들끼리 키 차이를 저장하고 어떤 부분에서 큰 차이가 난지 알기 위해서 index까지 같이 저장해준다.
    3. 차이를 저장한 리스트를 내림차순 정렬해서, k개의 그룹을 만들면 그게 최소비용
    4. k개의 그룹을 만들려면 k-1개로 나누어서 그룹을 분리하면 된다.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hs = list(map(int, input().split()))

diff = []
for i in range(1, n):
  difference = hs[i] - hs[i-1]
  diff.append((difference, i))
  # diff.append((difference, hs[i], hs[i-1]))
diff.sort(key = lambda x:(x[0], x[1]), reverse = True)

cost = 0
# k개의 그룹을 만들기 위해서는, k-1개의 구분선을 그어야함
indexes = []
for i in range(k-1):
  indexes.append(diff[i][1])
indexes.sort()

start = 0
for index in indexes:
  # print(hs[index-1], hs[start])
  cost += (hs[index-1] - hs[start])
  # print("cost : " + str(cost))
  start = index
  # print("start : " + str(start))

# 마지막 그룹은 더해지지 않는 경우도 있어서, 해당 그룹의 비용 또한 더하기
if start != n-1:
  cost += (hs[n-1] - hs[start])
print(cost)
