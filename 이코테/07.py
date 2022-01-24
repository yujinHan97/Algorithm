'''
    알고리즘:
    1. 구현하라는 대로 하면 str의 왼쪽, str의 오른쪽의 합을 구해서 구현하면 쉬운 문제
'''
N = input()
pivot = len(N) // 2

left = N[:pivot]
right = N[pivot:]

left_sum, right_sum = 0, 0
for num in left:
  left_sum += int(num)

for num in right:
  right_sum += int(num)

if left_sum == right_sum:
  print("LUCKY")
else:
  print("READY")
