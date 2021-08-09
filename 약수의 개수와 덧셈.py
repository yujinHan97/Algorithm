'''
    * 제곱수는 약수의 개수가 홀수개, 그 외는 모두 짝수개

    따라서, isEven이라는 함수를 따로 정의하지 않고도 가능
        if (i**0.5) == (int)(i**0.5) --> 제곱수 판별
    
    def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (i**0.5) == (int)(i**0.5): 
            answer -= i
        else:
            answer += i
    return answer
'''
def isEven(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
            
    if count % 2 == 0:
        return True
    else:
        return False
    
def solution(left, right):
    answer = 0
    
    for a in range(left, right+1):
        if isEven(a):
            answer += a
        else:
            answer -= a
            
    return answer
