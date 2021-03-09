'''
    9251 LCS
    알고리즘: 
    (구글링 해서 대충은 풀었다. 아직도 잘 이해 안감.. 나중에 꼭 다시 풀어보기)
    1. 추가한 문자가 같은 경우, 추가되기 전 값 + 1
    2. 추가한 문자가 다른 경우, 추가되기 전 값들 중 큰 값
'''
s1 = input()
s2 = input()
len1 = len(s1)
len2 = len(s2)
dp = [[0] * (len2 + 1) for i in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len1][len2])