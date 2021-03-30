'''
    알고리즘:
    1. 음수 부호가 있으면 나중에 -1을 곱해주기
    2. 다른 방법으로는, 
       answer = int(s) 
       return answer 
       하면 끝난다
'''
def solution(s):
    answer = 0

    is_neg = False
    if s[0] == '-':
        is_neg = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    for i in range(len(s)):
        answer += (int(s[i]) * (10 ** (len(s)-i-1)))

    if is_neg == True:
        return -1 * answer
    else:
        return answer
