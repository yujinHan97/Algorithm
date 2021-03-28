'''
    11401 이항계수 3   
    알고리즘:
    (구글링하여 푼 문제)
    1. 페르마의 소 정리를 참고
'''
import sys
def power(a,b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a, b//2) ** 2 * a) % p
    else:
        return (power(a, b//2) ** 2) % p

p = 1000000007
N, K = map(int, input().split())

factorial = [1 for _ in range(N+1)]

for i in range(2, N+1):
    factorial[i] = factorial[i-1] * i % p

A = factorial[N]
B = (factorial[N-K] * factorial[K]) % p

# (A/B) % p
#= A * B^-1 % p
#= A * B^-1 * B^p-1 % p
#= A * B^p-2 % p
#= (A % p) * (B^p-2 %p) % p
print((A % p) * (power(B, p-2) % p) % p)