'''
    알고리즘:
    1. 스택 이용
'''
def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i]) 
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                return False
                
    if len(stack) == 0:
        return True
    else:
        return False
    
