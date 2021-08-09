'''
    1920 수 찾기
    알고리즘:
    1. B의 요소값들을 A에서 찾기위해서 A를 정렬하고 이진탐색한다
'''
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))
A.sort()

for i in range(M):
    result = binary_search(A, B[i], 0, N-1)
    
    if result == None:
        print(0)
    else:
        print(1)