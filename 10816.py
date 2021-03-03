'''
    10816 숫자 카드2
    알고리즘:
    1. 같은 수의 개수를 구할 때 bisect_left, bisect_right의 차이를 이용하면 쉽게 구할 수 있다
'''
import sys
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
num = list(map(int, sys.stdin.readline().split()))
cards.sort()

for i in range(M):
    a = bisect_left(cards, num[i])
    b = bisect_right(cards, num[i])
    print(b-a, end = ' ')