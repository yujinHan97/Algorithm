'''
    알고리즘
    1. 문제에 나와있는 요구사항 그대로 구현
    2. 문자의 개수를 셀 때 count()함수 사용
'''
def solution(s):
    answer = True
    
    s = s.lower()
    pcount = s.count('p')
    ycount = s.count('y')
    
    if pcount == ycount:
        return True
    else:
        return False

    return True
