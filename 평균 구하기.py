'''
    알고리즘: 
    1. 총합을 구하고 len으로 나눠 평균 구하기 
'''
def solution(arr):
    answer = 0
    
    total = sum(arr)
    answer = total / len(arr)
    
    return answer
