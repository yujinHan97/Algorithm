'''
    2696 중앙값 구하기
    (다시 풀어볼 것!)
    --> 원래 힙 하나로 해서, 매번 힙 정렬을 하고 중앙값을 출력했는데 시간초과!
    --> 2개의 힙을 사용해서 중앙값을 구하기! (최대힙과 최소힙을 이용)
    알고리즘 :
    1. 왼쪽 그룹은 최대힙을 이용하고 오른쪽 그룹은 최소힙을 이용
    2. 그러면 항상 왼쪽 그룹과 오른쪽 그룹의 중앙에는 중간값이 있다
'''
import heapq, sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    nums = []

    if M % 10 == 0:
        for _ in range(M // 10):
            nums.extend(list(map(int, input().split())))
    else:
        for _ in range(M // 10 + 1):
            nums.extend(list(map(int, input().split())))
            
    lheap = [] # 최대힙 
    rheap = [] # 최소힙
    mid = []
    for i in range(len(nums)):
        if len(lheap) == len(rheap):
            heapq.heappush(lheap, -nums[i]) # 최대힙이니까 -붙여서 넣기
        else:
            heapq.heappush(rheap, nums[i])

        if lheap and rheap:
            a = -lheap[0]
            b = rheap[0]

            if a > b:
                heapq.heappop(lheap)
                heapq.heappop(rheap)
                heapq.heappush(lheap, -b)
                heapq.heappush(rheap, a)
            
        if i % 2 == 0:
            mid.append(-lheap[0])


    print(len(mid))
    for i in range(len(mid)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(mid[i], end=' ')
    print()
