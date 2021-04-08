'''
    알고리즘: 
    1. 짝수면 even, 홀수면 odd를 더해 출력    1. 짝수면 even, 홀수면 odd를 더해 출력
'''
def solution(num):
    answer = ''
    
    if num % 2 == 0:
        answer += 'Even'
    else:
        answer += 'Odd'
        
    return answer
