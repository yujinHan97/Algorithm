'''
    10773 제로
    알고리즘:
    1. 스택을 이용해서 sum 출력
'''
import sys
K = int(input())
money = []

for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        money.pop()
    else:
        money.append(N)

print(sum(money))