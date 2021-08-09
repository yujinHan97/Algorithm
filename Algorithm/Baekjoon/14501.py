'''
    14501 퇴사
    알고리즘:
    1. 해당 일에서 걸리는 시간 > 퇴사 날인 경우, 그 상담은 하지 못하는 거니까 dp = 0
    2. 해당 일에서 걸리는 시간 < 퇴사 날인 경우, 
       이전에 상담했던 날에서 걸리는 시간이 현재 날 이하인 경우, 이전 것까지 더해서 max로 dp 수정
       이전에 상담했던 날에서 걸리는 시간이 현재 날 초과인 경우, 그냥 현재 dp와 p중에서 max로 dp 수정
'''
import sys
N = int(input())
t = [0]
p = [0]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

dp = [0] * (N+1)

if 1 + t[1] > N + 1:
    dp[1] = 0
else:
    dp[1] = p[1]
for i in range(2, N+1):
    for j in range(1, i):
        if (i + t[i] > N+1):
            dp[i] = 0
            continue

        if(j + t[j]<=i):
            dp[i] = max(dp[i], dp[j]+p[i])
        else:
            dp[i] = max(dp[i], p[i])

print(max(dp))