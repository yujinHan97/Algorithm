'''
    알고리즘:
    1. n의 나머지를 구하고 n을 10씩 나누기 반복, n이 굉장히 큰 수였는데 시간초과는 안남
    * 다른 풀이 : 
    return list(map(int, reversed(str(n))))
'''
def solution(n):
    answer = []
    
    while n != 0:
        answer.append(n%10)
        n //= 10
        
    return answer
