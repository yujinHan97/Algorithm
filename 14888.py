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

