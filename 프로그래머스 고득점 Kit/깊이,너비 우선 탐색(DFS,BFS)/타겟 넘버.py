'''
    알고리즘:
    1. numbers 리스트에서 하나씩 순서대로 빼면서 처음에는 +, - 저장하고 그 다음에는 연산
    2. deque를 이용해서 +, - 계산한 결과를 담기
'''
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    
    while numbers:
        # numbers에서 순서대로 하나씩 빼기 위함
        num = numbers.pop(0)
        
        # 처음에는 일단 맨 첫 숫자의 +, -를 q에 넣기
        if len(q) == 0:
            q.append(-num)
            q.append(num)
        # 그 외에, 숫자가 q에 있으면 
        else:
            temp =  []
            while q: # 임시로 q에 있는 모든 원소들을 temp에 넣고
                temp.append(q.popleft())
            for t in temp: # temp에 있는 개수 만큼 num과 +, -한 결과를 다시 q에 넣는다
                q.append(t+num)
                q.append(t-num)
                
    # q에는 최종 결과들이 들어있을 것이고, 그 중 target의 개수를 출력하면 된다
    return q.count(target)
