# 올바른 괄호 문자열인지 판단하는 함수
def isPerfect(p):
    stack = []

    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        elif p[i] == ')':
            if stack:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

# u, v로 분리하는 함수
def sepUandV(p):
    u, v = '', ''
    for i in range(len(p)):
        u += p[i]
        
        if u.count('(') == u.count(')'):
            index = i
            break
    
    if index == len(p) - 1:
        v = ''
    else:
        v = p[index+1:]

    return u, v

def solution(p):
    answer = ''

    # 1단계
    if p == '':
        return ''

    # 2단계
    U, V = sepUandV(p)

    # 3단계    
    if isPerfect(U):
        # 3-1단계
        return U + solution(V)
    
    # 4단계
    else:
        # 4-1단계
        answer = '('
        # 4-2단계
        answer += solution(V)
        # 4-3단계
        answer += ')'
        # 4-4단계
        U = U[1:-1]
        for i in range(len(U)):
            if U[i] == '(':
                answer += ')'
            elif U[i] == ')':
                answer += '('

        # 4-5단계
        return answer
