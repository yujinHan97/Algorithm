'''
    11047 동전 0
    알고리즘:
    1. 동전의 종류(A_list)를 내림차순으로 정렬
    2. A_list를 K와 비교하면서 가장 가까운 종류를 찾기
    3. 가장 가까운 종류를 나눈 몫만큼 count횟수 더하고, K에서 그 돈만큼 빼는 과정 반복
'''
import sys
N, K = map(int, input().split())
A_list = []
count = 0
for i in range(N):
    A_list.append(int(sys.stdin.readline()))
A_list.sort(reverse = True)

for money in A_list:
    if money > K:
        continue
    else:
        count += (K // money)
        K %= money

print(count)
