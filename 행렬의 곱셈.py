'''
    알고리즘:
    (인덱스 때매 꽤 시간이 걸린 문제)
    1. 행렬 문제 같은 경우, 인덱스 써서 꼭 해볼 것
'''
def solution(arr1, arr2):
    answer = []
    
    col = len(arr2[0])
    for i in range(len(arr1)):
        temp_list = []
        for j in range(col):
            temp = 0
            for k in range(len(arr1[i])):
                temp += (arr1[i][k] * arr2[k][j])
            temp_list.append(temp)
        answer.append(temp_list)

    return answer
