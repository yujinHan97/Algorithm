'''
    알고리즘:
    1. 각 옷 종류에 따라 사전 자료형을 만들어서 종류의 수를 저장한다
    2. 각각의 옷 종류마다, 각각의 종류 or 입지 않는 것 까지해서 +1씩 곱하여 모든 경우의 수 구함
    3. 그 중에서 모두 안 입는 경우가 있기 때문에 -1 
'''
def solution(clothes):
    answer = 1
    
    c = {}
    for cloth in clothes:
        if cloth[1] in c.keys():
            c[cloth[1]] += 1
        else:
            c[cloth[1]] = 1
            
    for num in c.values():
        answer *= (num + 1)
    
    return answer - 1
