'''
    알고리즘:
    (참고한 사이트 : https://unie2.tistory.com/709)
    1. 각 방향을 정해서 선생님이 끝까지 움직이는 watch() 선언 
    2. 장애물을 설치했다가 다시 제거하는 걸 반복하면서 확인
'''
import sys
from itertools import combinations
input = sys.stdin.readline

# 각 방향으로 감시 (학생 발견 : True)
def watch(x, y, dir):
  # 왼쪽
  if dir == 0:
    while y >= 0:
      if school[x][y] == 'S':
        return True 
      if school[x][y] == 'O':
        return False
      y -= 1
  # 오른쪽
  elif dir == 1:
    while y < n:
      if school[x][y] == 'S':
        return True 
      if school[x][y] == 'O':
        return False
      y += 1
  # 위
  elif dir == 2:
    while x >= 0:
      if school[x][y] == 'S':
        return True 
      if school[x][y] == 'O':
        return False
      x -= 1
  # 아래
  elif dir == 3:
    while x < n:
      if school[x][y] == 'S':
        return True 
      if school[x][y] == 'O':
        return False
      x += 1

  return False 

# 장애물 세우고 선생님이 검사 (학생 발견 : True)
def observe():
  for x, y in teachers:
    for i in range(4):
      if watch(x, y, i):
        return True

  return False

n = int(input())
school, empty, teachers = [], [], []

for i in range(n):
  school.append(list(input().split()))
  for j in range(n):
    if school[i][j] == 'X':
      empty.append((i, j))
    if school[i][j] == 'T':
      teachers.append((i, j))

flag = False
for data in combinations(empty, 3):
  # 3개의 장애물을 일단 설치
  for x, y in data:
    school[x][y] = 'O'

  if observe() == False:
    # 발견하지 않았다면, 학생을 숨길 수 있는 것
    flag = True
    break

  for x, y in data:
    school[x][y] = 'X'

if flag:
  print("YES")
else:
  print("NO") 
  
