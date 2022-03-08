'''
    알고리즘:
    (나중에 다시 풀기)
    1. 재귀함수 이용해서 backtracking으로 풀었다
    2. 넘겨주는 패러미터로 값 조절
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
minimum, maximum = 1e9, -1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth+1, total + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        if total < 0:
            result = -total // nums[depth]
            result = -result
        else:
            result = total // nums[depth]
        dfs(depth+1, result, plus, minus, multiply, divide-1)
        
dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(maximum)
print(minimum)

----------------------------------------------------------------------------------------------------------------
'''
    알고리즘: (Brute Force 알고리즘으로 시간은 느리지만 맞춤)
    1. 모든 연산자의 순열을 생성 (permutations)
    2. zip 연산자로 숫자와 연산자의 계산을 하면서, 최대값과 최솟값 찾기
'''
import sys
from itertools import permutations
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
ops = []
for idx, num in enumerate(op):
  if num == 0:
    continue
  else:
    if idx == 0:
      operation = '+'
    elif idx == 1:
      operation = '-'  
    elif idx == 2:
      operation = '*'
    elif idx == 3:
      operation = '//'

  for i in range(num):
    ops.append(operation)

op_p = list(permutations(ops, n-1))

max_result, min_result = -INF, INF
for i in range(len(op_p)):
  result = arr[0]
  for num, opp in zip(arr[1:], op_p[i]):
    if opp == '+':
      result += num
    elif opp == '-':
      result -= num
    elif opp == '*':
      result *= num
    elif opp == '//':
      if result < 0:
        result = -result
        result = result // num
        result = -result
      else:
        result //= num
    
  max_result = max(max_result, result)
  min_result = min(min_result, result)

print(max_result)
print(min_result)
