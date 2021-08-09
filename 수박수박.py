'''
    알고리즘:
    1. 인덱스가 홀수/짝수에 따라 수/박 출력
'''
def solution(n):
    answer = ''

    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'

    return answer
