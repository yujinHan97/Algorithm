'''
    알고리즘:
    1. 문제가 요구하는 그대로 구현하면 된다
'''
def solution(num):
    answer = 0
    
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
            
        answer += 1
        
        if answer > 500:
            return -1
        
    return answer
