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
    
'''
dict를 이용해서 푸는 방법도 존재

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

dict = {}
for i in range(N):
    if cards[i] in dict.keys():
        dict[cards[i]] += 1
    else:
        dict[cards[i]] = 1

M = int(input())
arr = list(map(int, input().split()))

for i in range(M):
    if arr[i] in dict.keys():
        print(dict[arr[i]], end = ' ')
    else:
        print(0, end = ' ')
'''
