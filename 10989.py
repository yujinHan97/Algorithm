'''
    알고리즘:
    1. 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있고, 가장 큰수의 차이가 100만을 넘지 않으므로, 계수 정렬 이용
    2. 메모리 초과를 줄이기 위해서, 가장 큰수가 이미 10000이라고 주어졌으므로, 리스트 한개만 10001크기로 생성
'''
import sys

N = int(input())
counts = [0] * 10001

for i in range(N):
    counts[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(counts[i]):
        print(i)
