'''
    알고리즘:
    (풀이랑 거의 비슷하게 풀었지만, 참고했다. 내 원래 풀이랑 비슷한 url : https://tmdrl5779.tistory.com/142)
    1. 모든 지점에서 상하좌우 탐색해서 연합을 만든다
    2. 그렇게 연합 만들수 있을때까지 인구이동 한다
'''
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
countries = []
for i in range(n):
  countries.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def check_(x, y, index):
  united = []
  united.append((x, y))
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  union_count = 1
  union_sum = countries[x][y]

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0<= ny < n and visited[nx][ny] == False:
        diff = abs(countries[x][y] - countries[nx][ny])
        if l <= diff <= r:
          q.append((nx, ny))
          visited[nx][ny] = True
          union_count += 1
          union_sum += countries[nx][ny]
          united.append((nx, ny))

  for i, j in united:
    countries[i][j] = union_sum // union_count

count = 0
while True:
  visited = [[False]*n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        check_(i, j, index)
        index += 1
  
  if index == n*n: # visited 가 모두 False 이면, index가  n*n이 되니까 이때는 중단. 
    break

  count += 1

print(count)
