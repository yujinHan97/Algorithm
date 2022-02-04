'''
    알고리즘:
    (참고한 url : https://cotak.tistory.com/14)
    1. n, m이 작은 수여서, brute force 이용
    2. 입력을 받으면서, 빈 공간과 바이러스 공간을 각각 리스트에 넣는다 (좌표로)
    3. 빈 공간 중에서 3중 for문 사용해서, 3개의 벽을 고를 때마다 bfs 수행
    4. bfs 수행하고, 0의 개수를 세서 큰 경우 갱신
    5. 3개 벽 세우고 bfs 했으면 다시 그 벽 허물고 또 다른 3개의 벽 고르는 것 반복
'''
import sys, copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
area, virus, empty = [], [], []
max_num = 0

for i in range(n):
  row = list(map(int, input().split()))
  area.append(row)
  for j in range(m):
    if row[j] == 0:
      empty.append((i,j))
    elif row[j] == 2:
      virus.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(narea):
  q = deque([])
  visited = [[False] * m for _ in range(n)]
  cnt = 0
  global max_num

  for v in virus:
    q.append(v)

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if area[nx][ny] == 0 and visited[nx][ny] == False:
        q.append([nx, ny])
        visited[nx][ny] = True
        narea[nx][ny] = 2
  
  for i in range(n):
    cnt += narea[i].count(0)

  if max_num < cnt:
    max_num = cnt

# 3중 포문으로 3개의 벽 세우기
for i in range(len(empty)-2):
  for j in range(i+1, len(empty)-1):
    for k in range(j+1, len(empty)):
      x1, y1 = empty[i]
      x2, y2 = empty[j]
      x3, y3 = empty[k]

      # 3개 골라서 벽 세우고 나서, bfs
      area[x1][y1] = 1
      area[x2][y2] = 1
      area[x3][y3] = 1

      # 임시의 area 배열 만들어서 그 배열로 bfs 수행
      narea = copy.deepcopy(area)
      bfs(narea)

      # bfs 완료 후에는, 벽 다시 철거
      area[x1][y1] = 0
      area[x2][y2] = 0
      area[x3][y3] = 0

print(max_num)
