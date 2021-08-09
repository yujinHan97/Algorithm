'''
    알고리즘:
    1. deque를 사용하여 매 시간마다 자기 이후에 나오는 가격들에 대해서 가격이 지금보다 작으면 break
    2. 매 시간마다 일단은 초를 센다
'''
from collections import deque
def solution(prices):
    answer = []
    
    q = deque(prices)
    while q:
        now = q.popleft()
        
        time = 0
        for i in q:
            time +=1 
            if now > i:
                break
                
        answer.append(time)
        
    return answer
