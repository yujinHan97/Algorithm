'''
    알고리즘:
    1. 횟수에 따른 총 가격을 temp에 넣고
    2. temp와 원래 money를 비교해서 return한다
'''
def solution(price, money, count):
    temp = 0
    for i in range(1, count+1):
        temp += (price * i)
        
    if temp > money:
        return temp-money
    else:
        return 0
    
    #return answer
