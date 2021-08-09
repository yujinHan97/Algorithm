'''
    알고리즘:
    1. a와 b의 대소 관계에 따라 for문의 증감을 +1, -1로 정해서 
'''
def solution(a, b):
    answer = 0
    
    if a > b:
        for i in range(a, b-1, -1):
            answer += i 
    elif a < b:
        for i in range(a, b+1, 1):
            answer += i
    else:
        answer = a
        
    return answer
