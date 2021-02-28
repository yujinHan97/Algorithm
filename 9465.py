'''
    9465 스티커
    알고리즘:
    1. stickers의 점수들을 합한 걸 dp에 저장
    2. 2번째 전 4장의 스티커 중에서 바로 옆에 있는 걸 제외하고, max를 고른다
'''
import sys
T = int(input())

for i in range(T):
    n = int(input())
    stickers = []
    dp = [[0] * n for i in range(2)]

    for j in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
 
    for a in range(2, n):
        dp[0][a] = max(dp[0][a-2], dp[1][a-2], dp[1][a-1]) + stickers[0][a]
        dp[1][a] = max(dp[0][a-2], dp[0][a-1], dp[1][a-2]) + stickers[1][a]
   
    print(max(max(dp[0]), max(dp[1])))