'''
    알고리즘:
    (이코테 문제랑 비슷)
    1. 각 방향을 바라보고 방향에 따라서 좌표의 움직임 달라진다.
    2. F나 B이면, 방향에 따라 +, -를 하고 L이나 R이면 회전만 한다.
    3. 거북이가 움직인 모든 영역의 최소 직사각형 넓이는, 거북이가 움직인 x좌표의 최대 - 최소 값과 y좌표의 최대 - 최소값의 곱으로 구하면 된다. 
'''
t = int(input())
for _ in range(t):
  sx, sy = 0, 0
  moves = input()

  x = [sx]
  y = [sy]
  dir = 0 # 초기 거북이는 북쪽을 향함 
  # 북, 동, 남, 서
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  for move in moves:
    if move == 'F':
      nx = sx + dx[dir]
      ny = sy + dy[dir]
    elif move == 'B':
      nx = sx - dx[dir]
      ny = sy - dy[dir]
    elif move == 'L':
      if dir == 0:
        dir = 3
      else:
        dir -= 1  
    elif move == 'R':
      if dir == 3:
        dir = 0
      else:
        dir += 1
    
    if move != 'L' and move != 'R':
      x.append(nx)
      y.append(ny)
      sx, sy = nx, ny

  x.sort()
  y.sort()
  width = x[-1] - x[0]
  height = y[-1] - y[0]
  print(width * height)
