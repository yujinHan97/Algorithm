'''
    알고리즘:
    1. 최소공배수, 최대공약수 구하는 건 보통 2개의 수에 관해 했음
    2. 이 점을 이용하여 배열을 정렬하고 2개씩 묶어서 최소공배수를 구하고,
       구한 그 최소공배수와 그 다음 요소의 최소공배수를 구하는 것을 반복
'''      
# 더 나은 풀이
def getGCD(a, b):
    if b == 0:
        return a

    return getGCD(b, a%b)

def solution(arr):    
    answer = 1
    arr.sort(reverse = True)
    
    for i in range(len(arr)-1):
        gcd = getGCD(arr[i], arr[i+1])
        arr[i+1] = gcd * (arr[i] // gcd) * (arr[i+1] // gcd)

    return arr[-1]

# 내 풀이
from collections import deque
def getGCD(a, b):
    if b == 0:
        return a

    if a >= b: # 이미 내림차순 정렬 해서 if문 필요 X
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
