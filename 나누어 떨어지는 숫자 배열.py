'''
    알고리즘:
    1. 문제의 요구사항을 그대로 구현
'''
def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0: # 나누어 떨어지면 넣기
            answer.append(i)
            
    if len(answer) == 0: # 모든 원소가 나누어 떨어지지 않는다면, -1 넣기
        answer.append(-1)
    else: # 나누어 떨어지는 수들을 오름차순 정렬
        answer.sort()

    return answer
