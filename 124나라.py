''' 
    알고리즘:
    1. 1,2,4만 사용하므로, 3을 기준으로 나눈 몫과 나머지를 활용하여 문제를 풀었다
'''
from collections import deque
def solution(n):
    answer = ''
    
    country124 = deque([])
    p = n // 3 # 몫
    q = n % 3 # 나머지
    country124.append(q)

    if q == 0:
        p -= 1
        
    while p >= 3:
        temp = p % 3
        p //= 3
        
        if temp == 0:
            p -= 1
        country124.appendleft(temp)
        
    country124.appendleft(p)
    
    if country124[0] == 0:
        country124.popleft()

    for num in country124:
        if num == 0:
            num = 4
        answer += str(num)
        
    return answer
