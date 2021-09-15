'''
    알고리즘:
    1. 너무 쉬운 문제, 그냥 하라는 대로 구현
'''
def solution(numbers):
    answer = 0
    
    #numbers.sort()
    for i in range(10):
        if i not in numbers:
            answer += i
            
    return answer
