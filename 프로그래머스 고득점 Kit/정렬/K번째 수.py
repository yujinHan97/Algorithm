'''
    알고리즘:
    1. i~j까지 수를 찾기 위해서 새로운 arr을 만들었지만, 인덱스때문에 i-1:j로
    2. 정렬 후, k번째 수를 추가
'''
def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
        
    return answer
