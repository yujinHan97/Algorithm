'''
    1934 최소공배수
    알고리즘:
    1.  최소공배수 = 최대공약수 * A,B의 몫으로 구할 수 있다.
    2.  최대공약수는 재귀함수를 이용하여 구함
'''
def gcd(A, B):
    if A % B == 0:
        return B
    else:
        return gcd(B, A%B)

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    
    yaksu = gcd(A, B)
    baesu = yaksu * (A // yaksu) * (B // yaksu)
    print(baesu)