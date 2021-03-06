'''
    11279 최대 힙
    알고리즘:
    1. 파이썬은 기본적으로 최소힙을 지원한다. 
    2. 따라서, push할 때는 -를 붙이고, pop할때는 -를 떼면된다
'''
import sys
import heapq

N = int(input())
q = []
result = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(q, -x)
    if x == 0:
        if not q: # 배열이 비어있는 경우
            result.append(0)
        else:
            result.append(-heapq.heappop(q))

for i in result:
    print(i)
