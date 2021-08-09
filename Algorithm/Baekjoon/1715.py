'''
    1715 카드 정렬하기
    알고리즘:
    (우선순위 큐를 써야한다는 생각을 하지 못했다
    --> 완전탐색을 하면, 카드 묶음을 합친 후에 그 횟수를 리스트에 넣고 또 정렬하니까 O(N^2)이다.
    --> 시간초과니까 더 빠른 우선순위 큐 활용)
    1. 제일 작은 묶음 2개를 선택해서 합치고 다시 다른 묶음을 선택하는 방법
    2. 우선순위 큐에 카드 묶음을 넣고,
    3. 2개의 묶음을 빼서 count수를 올리고, 두 묶음을 합친 횟수를 또 우선순위 큐에 넣기
'''
import sys, heapq

N = int(input())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))

h = [] 
for value in num: # 카드 묶음으로 우선순위 큐 구성
    heapq.heappush(h, value)

count = 0
while h:
    if len(h) == 1: # 우선순위 큐의 len이 1이라는 건, 끝까지 다 빼고 합한 결과값이 들어있다는 의미
        break

    # 우선순위 큐에서 2개를 빼서 더한 값은 다시 우선순위 큐에 넣고,
    # 더한 값 만큼 count 세기
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    count += (a+b)
    heapq.heappush(h, (a+b))

print(count)
