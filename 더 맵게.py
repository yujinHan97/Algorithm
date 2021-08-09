import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # heapify는 return 값 받을 변수 필요없다. 그냥 리스트를 힙으로 변환시키고 끝
    answer = 0

    while scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            
            new_scoville = first + 2 * second
            heapq.heappush(scoville, new_scoville)
            answer += 1
        else: # 여기서 answer = -1로 하면 시간초과이고 바로 return하면 시간초과 아님... 이것때매 오래걸렸다
            return -1

    return answer
