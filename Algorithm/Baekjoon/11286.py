'''
    11286 절댓값 힙
    알고리즘:
    1. 큐에 넣을때는 절댓값을 취한 값, 원래 값을 튜플 형태로 넣기
    2. 뺐을때 뒤의 값이 음수라면, -를 붙여서 출력
'''
import sys
import heapq

N = int(input())
q = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x > 0: 
        heapq.heappush(q, (x, x)) 
    elif x < 0: 
        heapq.heappush(q, (-x, x))
    else:
        if not q: # 배열이 비어있는 경우
            print(0)
        else:
            a, b = heapq.heappop(q)
            if b < 0:
                a = -a
            print(a)