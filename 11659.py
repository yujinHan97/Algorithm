'''
    알고리즘:
    (처음에 누적합으로 하지 않고 sum() 함수 썼는데 시간초과)
    1. 구간 합을 구하려면 누적 배열을 만들어서 j인덱스의 누적합에서 i-1인덱스 전을 빼면 구간합임 
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cum_arr = []
cum_arr.append(arr[0])
for i in range(1, len(arr)):
    cum_arr.append(cum_arr[i-1] + arr[i])

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1 or j == 1:
        print(cum_arr[j-1])
    else:
        print(cum_arr[j-1]- cum_arr[i-2])
