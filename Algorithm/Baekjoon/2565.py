'''
    2565 전깃줄
    알고리즘: 
    ( 구글링해서 알고리즘을 보고 구현하였다. 나중에 다시 할것)
    1. wire를 a전봇대 기준으로 정렬하고, b에 대해서 증가하는 부분 수열을 구함
    2. 가장 적은 전깃줄을 없애는 방법 == 가장 많은 전깃줄을 그대로 놔두는 것
    3. b전봇대 중에서 가장 긴 증가하는 수열의 길이를 찾고, 전체 에서 뺀다
'''
import sys
N = int(input())
wire = []
for i in range(N):
    wire.append(list(map(int, sys.stdin.readline().split())))

# wire를 앞에꺼를 기준으로 정렬한다
wire.sort(key = lambda x:x[0])
array = []
for i in range(N):
    array.append(wire[i][1])
dp = [1] * 500 # 줄 번호는 500이하의 자연수

# 연결된 wire에서 증가하는 부분수열을 찾는다
for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

maxv = max(dp)
print(N-maxv)