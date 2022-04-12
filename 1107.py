'''
    알고리즘:
    (처음에는 BFS로 해서, +1, -1로 갈 수 있는 곳을 찾아서 하려고 했으나 -> 메모리 초과, 인덱스 에러)
    1. 100에서 +, -로만 움직이는 횟수와
    2. 누를 수 있는 수에서 +, -로 움직이는 횟수 중 적은 횟수로 가능한 번호를 고른다
    3. n이 50만 이하니까 브루트포스로 접근해도 시간초과 X
    (아래에서 올라가는 것, 위에서 내려가는 것 고려해서 1000001까지 범위)
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m != 0:
  nums = list(map(int, input().split()))
else:
  nums = []

# 100에서 +, -로 움직이는 횟수
ans = abs(n-100)
for i in range(1000001):
  numArr = list(str(i))

  flag = False
  for k in numArr:
    if int(k) in nums:
      flag = True
      break

  if flag:
    continue
  else:
    # n-i : +, - 누르는 횟수
    # len(str(i)) : 누르는 번호의 개수
    ans = min(ans, abs(n-i) + len(str(i)))

print(ans)
