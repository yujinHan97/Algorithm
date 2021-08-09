'''
    알고리즘:
    1. 조합을 이용해서 3개의 숫자를 고르는 가능한 경우를 모두 고려한다
    2. 3개의 합에 대해서 소수이면 횟수를 +1 하는 경우를 완전탐색한다
'''
from itertools import combinations # 조합 사용 위해서 import

# 소수인지 판별하는 함수
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
def solution(nums):
    answer = 0
    
    # 3개의 조합에 대해서 탐색
    for i in list(combinations(nums, 3)):
        total = sum(i) # 3개의 수를 더한 값
        
        if is_prime(total):
            answer += 1
    
    return answer
