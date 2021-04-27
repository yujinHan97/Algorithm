'''
    알고리즘:
    1. 최대공약수 구하는 함수를 따로 정의한다
    2. 최소공배수는 최대공약수를 이용하여 구한다
'''
# 최대공약수 구하는 함수
def gcd(a, b):
    if a <= b:
        a, b = b, a
    
    # 나누어 떨어지면 그냥 그게 최대공약수
    if a % b == 0:
        return b
    # 나누어 떨어지지 않는다면, 재귀호출
    else:
        return gcd(b, a%b)
    
def solution(n, m):
    answer = []
    
    yak = gcd(n, m)
    bae = yak * (n/yak) * (m/yak)
    answer.append(yak)
    answer.append(bae)
        
    return answer
