'''
    1927 최소 힙
    알고리즘:
    1. heapq 라이브러리 사용
'''
import sys
import heapq

N = int(input())
q = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x > 0: 
        heapq.heappush(q, (x)) 
    elif x == 0:
        if not q: # 배열이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(q))