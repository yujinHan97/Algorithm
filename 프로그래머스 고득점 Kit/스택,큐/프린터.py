'''
    알고리즘:
    1. 나중에 location에서 찾아야하기 때문에 중요도와 index를 튜플로 묶어서 덱에 넣는다
    2. 먼저 덱의 맨 앞에서 꺼내고, 덱의 나머지랑 비교를 해서 젤 큰 값이면 그냥 인쇄
    3. 큰 값이 하나라도 있다면, 다시 뒤로 넣는다
    4. 인쇄가 가능한 애들은 complete에 넣는다
    5. complete에서 location이랑 같은 수를 찾으면, enumerate의 idx를 찾아서 +1하여 반환 
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    for idx, pri in enumerate(priorities):
        q.append((pri, idx))

    complete = []
    while q:
        temp = q.popleft()
        
        canPrint = True
        for i in range(len(q)):
            if temp[0] < q[i][0]:
                q.append(temp)
                canPrint = False
                break
        
        if canPrint:
            complete.append(temp)
    
    for idx, comp in enumerate(complete):
        if comp[1] == location:
            answer = idx + 1
            
    return answer
