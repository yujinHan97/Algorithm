'''
    알고리즘:
    1. 너무 쉬운 문제라 그냥 문제 적힌대로 구현
'''
def solution(s):
    answer = ''
    
    nums = list(map(int, s.split()))
    min_v = min(nums)
    max_v = max(nums)
    
    answer += str(min_v) + " " + str(max_v)
    
    return answer
