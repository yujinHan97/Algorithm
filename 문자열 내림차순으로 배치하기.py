'''
    알고리즘:
    1. 문자열을 sort하기 위해서, list로 변환해주고, sort한 후, string으로 join시켜준다
'''
def solution(s):
    answer = ''
    
    s = list(s)
    s.sort(reverse = True)
    answer = ''.join(s)
    
    return answer
