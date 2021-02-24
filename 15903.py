'''
    15903 카드 합체 놀이
    알고리즘:
    1. 카드를 합체할 때마다 카드들을 정렬해서 가장 앞에 있는 두 카드를 더한다
    2. 그 두 카드의 합으로, 두 카드의 수를 갱신하는 것을 반복
'''
import sys

n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))

for times in range(m):
    cards.sort()
    newvalue = cards[0] + cards[1]

    cards[0] = cards[1] = newvalue

print(sum(cards))