'''
    1932 정수삼각형
    알고리즘:
    1. 삼각형을 위에서부터 아래로 내려가면서 합을 구한다.
    2. 이때 젤 왼쪽 변과 젤 오른쪽 변은 그냥 위의 합과 자기 자신을 더하면 된다.
    3. 그러나 삼각형 변이 아닌 안쪽에 있는 경우, 위에서의 최대값을 골라서 자기 자신과 더해야 한다.
'''
N = int(input())
tri = []
dp = [[0] *N for i in range(N)]
for i in range(N):
    tri.append(list(map(int, input().split())))
    if i == 0:
        dp[i][0] = tri[i][0]
    
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        
        if i == j:
            dp[i][j] = dp[i-1][j] + tri[i][j]

        dp[i][j] = max(dp[i-1][j-1]+tri[i][j], dp[i-1][j] +tri[i][j])

max_value = 0
for i in range(N):
    for j in range(i+1):
        if dp[i][j] > max_value:
            max_value = dp[i][j]

print(max_value)