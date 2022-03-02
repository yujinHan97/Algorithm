'''
    알고리즘:
    1. q를 이중으로 돌면서 배포가능한 개수를 센다
    2. 개수를 세면 그 작업 또한 큐에서 빼는 것을 반복 
'''
from collections import deque

def solution(progresses, speeds):
    answer = []

    days = deque()
    todos = []
    for i in range(len(progresses)):
        todo = (100-progresses[i]) / speeds[i]
    
        if todo != int(todo): # 할 작업이 딱 떨어지지 않는 일 수라면, 나머지 작업을 위해서 하루를 더함
            todo = int(todo) + 1 
        days.append((i, int(todo)))

    while days:
        day = days.popleft() # 첫번째 작업마다 일단 빼고 배포의 수를 1로 초기화
        count = 1
         
        while days: # 그 다음 작업마다 배포가능한지를 확인
            new_day = days[0]
            if new_day[1] <= day[1]:
                count += 1
                days.popleft()
            else:
                break

        answer.append(count)
    return answer
