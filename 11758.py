'''
    알고리즘:
    1. 첫번째 점과 두번째 점의 직선의 방정식을 구하고 y값과 세번째 점의 x좌표를 넣은 값을 y3의 값을 비교
    2. y > y3 이면 직선 아래에 세번째 점이 있는 것 => 시계 방향(-1)
    3. y < y3 이면 직선 위에 세번째 점이 있는 것 => 반시계 방향(1)
    4. 그 외는 한 직선(0) 
    ** 직선의 방정식에서 zero division 발생할 수 있어서 x증가량은 양쪽 변에서 모두 신경 쓰지 말 것!
'''
coord = []
for i in range(3):
  x, y = map(int, input().split())
  coord.append((x, y))

if (coord[1][1] - coord[0][1]) * (coord[2][0] - coord[0][0]) > (coord[2][1] - coord[0][1]) * (coord[1][0] - coord[0][0]):
  print(-1)
elif ((coord[1][1]-coord[0][1]) * (coord[2][0] - coord[0][0])) < ((coord[2][1] - coord[0][1]) * (coord[1][0] - coord[0][0])):
  print(1)
else:
  print(0)
