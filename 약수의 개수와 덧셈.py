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
