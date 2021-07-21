'''
    기능개발
    알고리즘:
    1. 남은 일수를 rest 덱에 넣고 한 작업씩 빼기
    2. 작업 뺄 때마다 이 다음의 작업보다 오래걸리는 작업인 경우에는, 이 이후의 작업들을 뺄 수 있어서 temp에 넣고 count를 answer에 넣는다
'''
from collections import deque
def solution(progresses, speeds):
    answer = []
    rest = deque()

    for i in range(len(progresses)):
        temp = 100 - progresses[i]
        if temp/speeds[i] != int(temp/speeds[i]):
            rest.append(int(temp/speeds[i] + 1))
        else:
            rest.append(temp//speeds[i])
            
    while rest:
        temp = []
        num = rest.popleft()
        temp.append(num)

        while rest and temp[0] >= rest[0]:
            num = rest.popleft()
            temp.append(num)

        answer.append(len(temp))
        
    return answer
