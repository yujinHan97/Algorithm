'''
    알고리즘:
    1. 괄호를 회전할 때마다 완벽한 괄호인지 확인 ==> 모든 경우의 수를 매번 확인
'''
def isPerfect(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

def solution(s):
    answer = 0


    for i in range(len(s)):
        if i == 0:
            flag = isPerfect(s)
        else:
            s += s[0]
            s = s[1:]
            print(s)
            flag = isPerfect(s)

        if flag:
            answer += 1

    return answer
