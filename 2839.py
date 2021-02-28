'''
    2839 설탕배달
    알고리즘:
    1. 초반에 dp리스트를 무한대로 초기화하고, 3이랑 5는 배달할 수 있으니까 1로 설정
    2. 입력받은 설탕의 무게까지 탐색을 하는데, 설탕에서 3빼고, 5뺀 결과에 +1을 한 결과 중 최솟값을 dp에 저장
'''
import sys

N = int(input())
dp = [sys.maxsize] * 5001
dp[3] = dp[5] = 1

for i in range(6, N+1): # 3으로 배달하거나 5로 배달하는 것 중 최솟값 고르기
    dp[i] = min(dp[i-3]+1, dp[i-5]+1) 

if dp[N] >= sys.maxsize: # maxsize 이상이면, 만들 수 없는 거니까 -1
    print(-1)
else:
    print(dp[N])