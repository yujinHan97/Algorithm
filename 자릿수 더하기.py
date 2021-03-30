'''
    알고리즘:
    1. n을 10으로 나눈 나머지를 더하고, 10을 나누고를 반복
    
'''
def solution(n):
    answer = 0

    while n != 0:
        k = n % 10
        answer += k
        n //= 10

    return answer
