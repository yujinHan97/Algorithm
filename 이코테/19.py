'''
    알고리즘:
    (dfs/bfs 사용 안하고 pypy3로 제출해서 맞음, 책에는 중복 순열을 사용했지만
    나는 순열을 사용. 왜 중복 순열인지 아직 이해 안감)
    1. N이 최대 11이니까 모든 경우의 수는 (N-1)! 이어서 완전탐색 수행
    2. 모든 연산에 대해서 최대와 최소를 저장하여 구현
'''
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))
op = []
for i in range(4):
  if i == 0:
    for j in range(ops[0]):
      op.append('+')
  elif i == 1:
    for j in range(ops[1]):
      op.append('-')
  elif i == 2:
    for j in range(ops[2]):
      op.append('*')
  else:
    for j in range(ops[3]):
      op.append('/')

permuts = permutations(op, n-1)
max_result = -int(1e9)
min_result = int(1e9)

for x in permuts:
  for i in range(len(numbers)):
    if i == 0:
      result = numbers[i]
    else:
      nextNum = numbers[i]
      if x[i-1] == '+':
        result += nextNum    
      elif x[i-1] == '-':
        result -= nextNum
      elif x[i-1] == '*':
        result *= nextNum
      else:
        if result < 0 and nextNum > 0:
          result = -1 * ((-1*result) // nextNum)
        else:
          result //= nextNum

  if result > max_result:
    max_result = result
  if result < min_result:
    min_result = result

print(max_result)
print(min_result) 
