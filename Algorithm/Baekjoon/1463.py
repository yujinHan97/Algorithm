'''
    1463 1로 만들기
    알고리즘:
    1. 각 수에 대해서, -1, //3, //2 연산을 해본다
    2. 그리고, -1, //3, //2 중에 최소 연산 횟수를 고른다
'''
X = int(input())
dp = [0] * 1000001
for i in range(2, X+1):
    dp[i] = dp[i-1]+1

    if i % 3 ==0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[X])