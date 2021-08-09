'''
    알고리즘:
    1. 숫자인지 확인하는 함수 isdigit() 사용
'''
def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        answer = False
        
    for ch in s:
        if ch.isdigit() == False:
            answer = False
            break
    
    return answer
