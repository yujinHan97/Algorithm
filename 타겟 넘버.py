'''
    이런 문제도 DFS/BFS로 풀 수 있다는 것 알기! 
    완전 탐색해도 시간 범위내에 나올수 있음
    맨 처음에 BFS 함수를 따로 빼서 했고, while deq 이게 맞나 싶엇는데 다시 풀어보기
    (DFS, 다른 방법 또 있음 풀어보기!)
'''
from collections import deque
def solution(numbers, target):
    deq = deque([(0, 0)])
    answer = 0
    
    while deq:
        sum, index = deq.popleft()

        if index == len(numbers):
            if sum == target:
                answer += 1
        else:
            number = numbers[index]
            deq.append((sum + number, index+1))
            deq.append((sum - number, index+1))
    
    return answer
