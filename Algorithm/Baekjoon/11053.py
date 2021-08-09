'''
    11053 가장 긴 증가하는 부분 수열
    알고리즘:
    1. 자기 자신보다 작은 수의 개수를 dp에 저장
    2. dp를 갱신할 때, 자기 앞의 dp중에서 가장 max값을 찾고, 그 값을 더해서 갱신
'''
import sys
N = int(input())
A = [0]
data = list(map(int, sys.stdin.readline().split())) 
A.extend(data)
dp = [1] * (N+1)
dp[0] = 0

for i in range(2, N+1):
    maxdp = 0
    for j in range(i-1, 0, -1):
        if A[i] > A[j]: # i-1번째 이하의 수에 대해서, 현재 값보다 작으면, 그 중에서 maxdp값을 찾는다
            if maxdp < dp[j]: 
                maxdp = dp[j]            
    dp[i] += maxdp

print(max(dp))
