'''
    알고리즘:
    1. arr에 1개의 수만 있다면, 그게 가장 작은 수이고 제거하면 빈 배열이므로 -1 채워서 리턴
    2. 그게 아니라면, min을 구해서 그 수만 제거하고 리턴
'''
def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        return answer
    else:
        min_num = min(arr)
        arr.remove(min_num)
        answer = arr
        return answer
