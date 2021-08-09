'''
    9461 파도반수열
    알고리즘:
    1. 수를 나열해보면, 1 1 1 2 2 3 4 5 7 9 12 16 21 ...이 된다.
    2. N번째 수를 구하기 위해서, 앞의 수 + 5번 더 앞선 수를 해서 뒤의 수가 되는 과정이 반복된다
    3. 이 때, dp가 0이아니면 이미 연산된 결과이므로 그냥 넘어가면 된다
'''
import sys
T = int(input())
dp = [0] * 100
dp[0] = dp[1] = dp[2] = 1
dp[3] = dp[4] = 2

for i in range(T):
    N = int(input())
    
    for i in range(5, N):
        if dp[i] != 0:
            continue
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N-1])