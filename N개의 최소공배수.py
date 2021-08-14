'''
    알고리즘:
    1. 최소공배수, 최대공약수 구하는 건 보통 2개의 수에 관해 했음
    2. 이 점을 이용하여 배열을 정렬하고 2개씩 묶어서 최소공배수를 구하고,
       구한 그 최소공배수와 그 다음 요소의 최소공배수를 구하는 것을 반복
'''      
from collections import deque
def getGCD(a, b):
    if b == 0:
        return a

    if a >= b:
        gcd = getGCD(b, a % b)
    else:
        a, b = b, a
        gcd = getGCD(b, a % b)
        
    return gcd

def solution(arr):    
    answer = 1
    arr.sort(reverse = True)
    
    qarr = deque(arr)
    while len(qarr) > 1:
        a = qarr.popleft()
        b = qarr.popleft()
        gcd = getGCD(a, b)
        answer = gcd * (a // gcd) * (b // gcd)
        qarr.appendleft(answer)

    return qarr[0]
