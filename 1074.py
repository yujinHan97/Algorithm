'''
    알고리즘:
    1. 4등분한 맨 왼쪽, 위 좌표를 기준으로 어떤 사분면에 해당하는지 quad로
    2. 계속 반복하고 4등분한 부분의 크기가 4가 되면 멈추기
'''
n, r, c = map(int, input().split())

num = 2 ** (n-1)
quad = 0
answer = 0
while True:
  part = num * num
  # 마지막이 되면 r,c에 따라 0,0 / 0,1 / 1,0 / 1,1 인지 파악해서 번수 구하기
  if part == 1:
    if r == 1 and c == 1:
      answer += 3
    elif r == 1:
      answer += 2
    elif c == 1:
      answer += 1
    break

  if 0<= r < num and 0 <= c < num:
    quad = 0
  elif 0 <= r < num and num <= c:
    quad = 1
  elif num <= r and 0 <= c < num:
    quad = 2
  else:
    quad = 3

  # 좌표 재정비(다른 부분 자른 경우에)
  if r >= num and c >= num:
    r -= num
    c -= num
  elif r >= num:
    r -= num
  elif c >= num:
    c -= num

  answer += (quad * part)
  num //= 2

print(answer)
