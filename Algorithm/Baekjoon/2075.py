'''
    2075 N번째 큰 수
    --> 메모리 (4MB) : int형 리스트 100만개 가능
    --> 다시 풀어볼 것!
    알고리즘:
    1. 메모리가 굉장히 제한적이므로, 입력을 받으면서 힙을 생성한다
    2. 힙의 사이즈를 항상 N으로 유지하기
'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    nums = list(map(int, input().split()))

    # 힙이 비어있는 경우는 그냥 heappush
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num: # 최소힙으로 구현되어있으니까, 제일 작은 것보다 크면 작은값 빼고 큰 값 넣기
                heapq.heappop(heap)
                heapq.heappush(heap, num)

# 최종적으로 사이즈가 N인 힙이 남는데, 그 힙은 최소힙이니까 가장 앞 원소가 N번째로 큰 원소이다
print(heap[0])
