'''
    알고리즘:
    1. 에라토스테네스의 채 사용
    * 에라토스테네스의 채 : 찾고자 하는 수(n)까지 True로 초기화한 리스트를 생성한 후,
                          2를 제외한 2의 배수, 3을 제외한 3의 배수, 5를 제외한 5의 배수, ... sqrt(n)의 배수는 모두 False로
                          2부터 n까지 True인 수들이 소수
'''
def solution(n):
    answer = 0
    
    is_sosu = [True] * (n+1)
    m = int(n ** 0.5) # 루트 n ==> n ** 0.5

    for i in range(2, m+1): # n의 최대 약수가 sqrt(n) 이하
        if is_sosu[i] == True:
            for j in range(2*i, n+1, i): # i를 제외한 i의 배수에 대해서, False로
                is_sosu[j] = False

    for i in range(2, n+1):
        if is_sosu[i] == True:
            answer += 1

    return answer
