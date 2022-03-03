'''
    알고리즘:
    1. heapify로 힙을 구성해서, 2개씩 빼고 새로운 scoville을 계산해서 넣는 것을 반복
    2. 만약 첫번째 뺀게 K이상이면, 모든게 K이상이므로 그만두면 된다
    3. 만약 첫번째 뺐을 때 남은게 없다면, 결국 못만드는 뜻이므로 -1을 return
'''
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while True:
        a = heapq.heappop(scoville)
        
        if a >= K:
            break
        if len(scoville) == 0:
            return -1

        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)
        answer += 1

    return answer
