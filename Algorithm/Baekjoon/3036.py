''' 
    3036 링
    알고리즘:
    1. 첫번째 링 / i번째 링을 해서 각 링이 돌아가는 식 구하기
    2. 기약분수로 나타내기 위해서 gcd 최대공약수 구해서 나누기 
'''

def gcd(A, B):
    if A % B == 0:
        return B
    else:
        return gcd(B, A % B)

N = int(input())
ring = list(map(int, input().split()))

for i in range(1, N):
    a = ring[0]
    b = ring[i]

    k = gcd(a, b)
    a = a // k
    b = b // k

    num = [str(a), str(b)]
    print("/".join(num))