'''
    알고리즘:
    1. 합을 리스트에 넣고, 중복된 결과가 있을 수 있으므로 set() 함수 적용
'''
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    answer = list(set(answer))
    answer.sort()
    
    return answer
