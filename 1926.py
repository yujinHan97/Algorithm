'''
    알고리즘:
    1. bfs를 사용해서, 1이 있으면 그림의 개수를 +1
    2. 1이 발견될 때 마다, 0으로 바꾸고 1의 개수를 세기
    +) 처음에 count가 1이고 size가 1인 경우일 때 틀렸음 --> p_size를 처음에 0으로 초기화했기 
'''
from collections import deque
def bfs(i, j):
  q = deque()
  q.append((i, j))
  paper[i][j] = 0
  global p_size
  p_size = 1
  
  while q:
    x, y = q.popleft()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for a in range(4):
      nx = x + dx[a]
      ny = y + dy[a]

      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if paper[nx][ny] == 1:
          paper[nx][ny] = 0
          p_size += 1
          q.append((nx, ny))

n, m = map(int, input().split())
paper = []
for i in range(n):
  paper.append(list(map(int, input().split())))

count = 0
area = []
for i in range(n):
  for j in range(m):
    if paper[i][j] == 1:
      count += 1
      bfs(i, j)
      area.append(p_size)

print(count)
if count == 0:
  max_area = 0
else:
  max_area = max(area)
print(max_area)
