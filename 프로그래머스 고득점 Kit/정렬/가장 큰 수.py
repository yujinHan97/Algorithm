'''
    알고리즘:
    1. 문자열로 4자리 수 만들어서 비교하는 것을 생각해내야 하는 문제
    2. 30, 5를 중에 숫자로는 30이 크지만, 문자열로는 5가 더 크기 때문
'''
def solution(numbers):
    answer = ''
    
    # TC 11번
    if sum(numbers) == 0:
        return '0'
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*4, reverse = True)
    answer = ''.join(numbers)
    
    return answer
