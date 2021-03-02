'''
    11053 가장 긴 바이토닉 부분 수열
    알고리즘:
    1. 자기 자신보다 작은 수의 개수를 dp에 저장
    2. 앞에서 부터 차례대로, 자기보다 작은 수 중에서 dp값이 최대인 수를 찾아 더하여 갱신
    3. 바이토닉 수열은 증가하다가 감소하니까, 바로 전의 단계를 반대로 수행하면 된다
    4. 뒤에서 부터 차례대로, 자기보다 작은 수 중에서 dp값이 최대인 수를 찾아 더하여 갱신
'''
import sys
N = int(input())    
A = [0]
data = list(map(int, sys.stdin.readline().split())) 
A.extend(data)
dp = [1] * (N+1)
dp[0] = 0
dp2 = [0] * (N+1)

# 앞에서 부터 탐색하고, S1<S2<...<Sk 하도록
for i in range(2, N+1):
    for j in range(1, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
     
# 뒤에서 부터 탐색해서, Sk>Sk+1 > ..>SN 하도록
for i in range(N-1, 0, -1):
    for j in range(i+1, N+1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(1, N+1):
    dp[i] = dp[i] + dp2[i]
print(max(dp))