'''
    알고리즘:
    (맨처음에는 deque로 풀었는데, 정확성은 100% 효율성은 0%.
    풀이방법 떠오르지 않아서 책 보고, 코드도 어려워서 참고함)
    1. 시간이 적게 걸리는 음식을 제거하는데, 그 음식을 다 먹기위한 싸이클 초를 구함
    2. 현재 먹은 시간 + (해당 음식 - 이전 음식먹을 때 걸린 시간) * 싸이클 <= k라면, 음식 뺄 수 있음
'''
import heapq

def solution(food_times, k):
    q = []
    
    if sum(food_times) <= k:
        return -1
    
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_time = 0
    prev_time = 0
    length = len(q)
    while sum_time + (q[0][0]-prev_time) * length <= k:
        now_time, num = heapq.heappop(q)
        sum_time += (now_time - prev_time) * length # 제일 작은시간을 빼가면서, 이전에 한 싸이클을 돌 때 시간을 빼기 위해서 prev_time 빼기
        length -= 1
        prev_time = now_time

    q.sort(key = lambda x:(x[1]))
    
    return q[(k-sum_time)%len(q)][1]
