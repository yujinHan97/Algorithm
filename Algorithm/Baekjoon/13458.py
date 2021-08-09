'''
    13458 시험감독
    알고리즘:
    1. 총감독관이 한 시험장에 1명 있어야 하므로, 모든 시험장마다 배치하고 총감독관이 관리하는 수 만큼 장소에서 뺀다
    2. 빼고 남은 사람들이 양수라면, 그 수에 대해서 부감독관을 부여한다
    3. 부감독관을 배치할 때, 배수라면 몫만큼 배치하고, 배수가 아니라면, 몫 + 1 만큼 배치한다
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for i in range(len(A)):
    A[i] -= B
    count += 1

for i in range(len(A)):
    if A[i] > 0: # 중요한 조건
        if A[i] % C == 0:
            count += (A[i] // C)
        else:
            count += (A[i] // C + 1)

print(count)
