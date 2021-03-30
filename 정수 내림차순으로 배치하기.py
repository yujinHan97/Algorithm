'''
    알고리즘:
    1. int를 list로 바꿔서 정렬 한 후, join
    2. join하면 str 형태니까 int형태로 
'''
def solution(n):    
    num = list(str(n))
    num.sort(reverse = True)

    return int(''.join(num))
