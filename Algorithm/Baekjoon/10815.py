'''
    10815 숫자카드
    알고리즘:
    1. 데이터의 개수가 많아서 이진탐색 이용
'''
import sys
def b_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
findings = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    result = b_search(cards, findings[i], 0, N-1)

    if result == None:
        print(0, end = ' ')
    else:
        print(1, end = ' ')