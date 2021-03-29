'''
    알고리즘:
    1. enumerate() 함수 써서 index 찾고 문자열로 
'''
def solution(seoul):
    answer = ''
    
    for idx, name in enumerate(seoul):
        if name == "Kim":
            break
            
    answer += '김서방은 '
    answer += str(idx)
    answer += '에 있다'
    
    return answer
