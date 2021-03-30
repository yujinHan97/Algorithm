'''
    알고리즘:
    1. 루트를 씌운 값이 정수이면(is_integer() 사용), 제곱근이므로, +1의 제곱 반환
    2. 아니면 -1 반환
    * is_integer() 대신, sqrt()한 값을 1로 나누었을 때 0이면 정수임을 
    if sqrt % 1 == 0:
'''
def solution(n):
    answer = 0
    
    m = n ** 0.5
    if m.is_integer() == True:
        answer = (m+1) ** 2
    else:
        answer = -1
        
    return answer
