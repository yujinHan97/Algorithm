'''
    알고리즘:
    1. solution() 함수를 재귀적으로 부르는 것을 참고하였다
    2. 문제에 제시된 대로 구현하면 된다
'''
# 올바른 괄호 문자열인지 판단하는 함수
def isPerfect(p):
    stack = []
    for paren in p:
        if paren == '(':
            stack.append(paren)
        elif paren == ')' and stack:
            stack.pop()
                
    if len(stack) == 0:
        return True
    else:
        return False
    
# u, v로 분리하는 함수
def seperate(p):
    openp, closep = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            openp += 1
        else:
            closep += 1
            
        if openp == closep:
            return i
        
def solution(p):
    answer = ''
    
    # 1단계
    if p == '':
        return ''
    
    # 2단계
    index = seperate(p)
    u = p[0:index+1]
    if index+1 >= len(p):
        v = ''
    else:
        v = p[index+1:]
        
    # 3단계
    if isPerfect(u):
        return u + solution(v)
    # 4단계
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer
