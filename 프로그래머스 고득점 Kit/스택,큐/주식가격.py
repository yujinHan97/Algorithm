'''
    알고리즘:
    1. 큐에서 맨 앞 원소를 한개씩 빼면서, 떨어지지 않은 만큼 count를 세면 된다.
    2. 떨어지자 마자 해당 가격은 중단하면 된다.
'''
from collections import deque

def solution(prices):
    answer = []
    
    q = deque(prices)
    while q:
        price = q.popleft()
        
        count = 0
        for qi in q:
            count += 1
            if price > qi:
                break
        answer.append(count)
        
    return answer
