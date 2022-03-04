'''
    알고리즘:
    1. j인덱스에 따라 0과 i가 아닐때에는 위의 양 대각선 중에서 큰 것을 골라서 내려온다
'''
def solution(triangle):    
    len_tri = len(triangle)
    dp = [[0] * len_tri for _ in range(len_tri)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[len_tri-1])
