'''
    알고리즘:
    1. 연속된 숫자의 합을 구하는 것이니까 n//2까지 누적합을 구해서 dict를 만든다
    2. dict에서 n과 같고, 누적합에서 n을 뺀 것도 key에 있으면 +1
'''
def solution(n):
    answer, cumm = 0, 0
    
    arr_dict = {}
    for i in range(1, (n//2)+2):
        cumm += i
        arr_dict[cumm] = 1
        
#    print(arr_dict)
    
    if n in arr_dict.keys():
        answer += 1

    for key in arr_dict.keys():
        if key - n in arr_dict.keys():
            answer += 1
            
    return answer + 1 # 아무것도 합이 아닌 자기 자신의 경우가 있어서 + 1
