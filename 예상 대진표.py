'''
    알고리즘:
    1. 2팀씩 동시에 진행하니까 log2(N)으로 최대가 될 것이고
    2. a와 b를 2씩 줄여나가면서 
        - 같으면 그 때 경기하는 것
        - 1차이가 나는데 큰 수가 짝수인 경우에는 경기하는 것
        - 1차이가 나는데 큰 수가 홀수인 경우에는 다음번에 경기하는 것 --> 1번 더 돌기
'''
import math

def solution(n,a,b):
    answer = 1
    
    for i in range(int(math.log2(n))):
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b //2 + 1
        max_val = max(a, b)

        if a == b:
            return answer
        if abs(a-b) == 1 and max_val % 2 == 0:
            return answer + 1
        else: 
            answer += 1
