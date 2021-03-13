'''
    알고리즘:
    1. commands에서 i, j, k를 받아서 array를 slicing 하고 정렬해서 k번째 구한다 
'''
def solution(array, commands):
    answer = []
    
    for a in range(len(commands)):
        i, j, k = commands[a][0], commands[a][1], commands[a][2]
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
        
    return answer
