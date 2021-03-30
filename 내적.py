'''
    알고리즘:
    1. a와 b는 길이가 같으므로, 같은 인덱스끼리 곱해서 총 더한 값 반환
'''
def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
        
    return answer
