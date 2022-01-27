'''
    알고리즘:
    (이렇게 해야겠다는 생각은 했으나, 구현을 제대로 못해서 풀이 참고함 => rotate 함수 다시 살펴보기)
    1. 사과가 있으면, 뱀의 길이부분을 q에 넣고 
    2. 사과가 없으면, 뱀의 꼬리부분 마지막을 빼서 다시 map 0으로 초기화하기
'''
n = int(input())
k = int(input())
maps = [[0] * n for _ in range(n)]
for _ in range(k):
  x, y = map(int, input().split())
  maps[x-1][y-1] = 1

l = int(input())
rot = []
for _ in range(l):
  sec, dir = map(str, input().split())
  rot.append((int(sec), dir))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def rotate(direction, dir):
  if dir == "L":
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4
  return direction

x, y = 0, 0
maps[x][y] = 2
game_time, direction = 0, 0
q = [(x, y)]
rot_index = 0

while True:
  nx = x + dx[direction]
  ny = y + dy[direction]

  if nx >= n or ny >= n or nx < 0 or ny < 0 or maps[nx][ny] == 2:
    game_time += 1
    break
  else:
    # 사과가 없는 경우라면, 일단 머리는 해당 위치에 넣는다
    # 꼬리를 댕겨와야하니까, 원래 뱀의 위치였던 걸 빼서 0으로 다시 set
    if maps[nx][ny] == 0:
      maps[nx][ny] = 2
      q.append((nx, ny))
      prev_x, prev_y = q.pop(0)
      # print("prev", end = "    ")
      # print(prev_x, prev_y)
      maps[prev_x][prev_y] = 0
    elif maps[nx][ny] == 1:
      maps[nx][ny] = 2
      q.append((nx, ny))
    game_time += 1
    x, y = nx, ny

    if rot_index < l and game_time == rot[rot_index][0]: # rot_index의 개수가 rot의 개수 l(알파벳 l)보다 작은 경우에만 해야 index error 발생 X
      dir = rot[rot_index][1]
      direction = rotate(direction, dir)
      rot_index += 1

print(game_time)
