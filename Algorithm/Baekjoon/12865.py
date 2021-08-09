''' 
    12865 평범한 배낭
    (구글에 검색해서 알고리즘과 풀이 참고한 문제. 나중에 다시 풀어볼것)
    1. dp[N][K]의 2차원배열을 생성
    2. i번째 아이템의 무게와 비교하면서 점화식 생성
       - i번째 아이템을 챙기지 않았을 때의 최댓값 : dp[i-1][j]
       - i번째 아이템을 챙겼을 때의 최댓값 : dp[i-1][j-wv[i][0]] + wv[i][1] 
         (무게는 i번째 아이템을 포함해서 j가 되도록 하기 위해서 j에서 i의 무게를 뺀 값에서 i번째 아이템의 value를 더한다)
'''
import sys

N, K = map(int, input().split())
wv = [[0, 0]]
for i in range(N):
    wv.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*(K+1) for i in range(N+1)] 

for i in range(1, N+1):
    for j in range(1, K+1):
        if wv[i][0] > j: 
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i][0]] + wv[i][1])

print(dp[N][K])