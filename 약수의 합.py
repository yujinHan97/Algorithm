'''
    알고리즘:
    1. 1부터 n까지 나누어지면, yaksu 리스트에 넣고 합 구하기
    # 다른 풀이 : 
    def solution(n):
        # n / 2 의 수들만 검사하면 성능 약 2배 향상, 그 수들의 sum과 n을 더해서 반환
        return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
'''
def solution(n):    
    yaksu = []
    for i in range(1, n+1):
        if n % i == 0:
            yaksu.append(i)
            
    return sum(yaksu)
