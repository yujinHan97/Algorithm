'''
    1026 보물
    알고리즘:
    1. S를 작게 만들기 위해서, A의 작은수 * B의 큰수가 되도록 A배열을 정리한다.
'''
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
new_A = [0] * N
dict = {}

for i in range(N):
    dict[i] = B[i]

b = sorted(dict.items(), key = lambda x:x[1], reverse = True)
A.sort()

sumv = 0
for i in range(N):
    sumv += (A[i] * b[i][1])
print(sumv)