'''
    짝지어 제거하기
    --> 스택을 생각하지 못하고 계속 시간초과가 나와서 답안을 보았다...!
    (스택 사용하란 것만 읽고 풀었더니 금방 맞춤..)
    --> 짝지어 제거하는 것 같은 유형은 스택으로 풀기! (괄호같은 것도)
    알고리즘:
    1. 스택 이용..
'''
def solution(s):
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0
