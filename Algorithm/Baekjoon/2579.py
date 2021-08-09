'''
    2579 계단 오르기
    알고리즘:
    1. 계단 올라가는 규칙을 고려해서, 점화식을 이용했다
    2. 마지막 계단을 기준으로, 그 전계단을 밟을 경우와, 그 전전계단을 밟을 경우로 나눴다
       - 전계단을 밟는 경우, 3번 연속 밟는 것을 방지해야 하므로, 3번째 전계단에서 올라오는 점화식
    3. 전계단을 밟는 경우와 전전계단을 밟는 경우 중에 최대값을 더한다
'''
import sys
floor = int(input())
score = [0]
dp = [0]*301
for i in range(floor):
    score.append(int(sys.stdin.readline()))

for i in range(1, floor+1):
    if i == 1:
        dp[i] = dp[i-1] + score[i]
    elif i == 2:
        dp[i] = dp[i-1] + score[i]

    else: # 계단이 3개 층 이상인 경우, 바로 전계단 / 두번째 전 계단 밟은 경우 중 큰 값에 밟을 계단을 더한게 최댓값
        dp[i] = max(dp[i-3] + score[i-1], dp[i-2]) + score[i] 
    
print(dp[floor])