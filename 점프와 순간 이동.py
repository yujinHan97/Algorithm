'''
    알고리즘:
    1. 현재 거리의 *2까지 갈 수 있으므로, 짝수의 거리라면 순간이동으로 바로 가능
    2. 그게 아니라면, 2로 나눈 나머지만큼은 점프를 해야함
'''
def solution(n):
    cnt = 0

    while n>0:
        cnt += n % 2
        n = n // 2

    return cnt
