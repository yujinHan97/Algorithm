'''
    2156 포도주 시식
    알고리즘:
    1. dp[i](= i번째까지 마시는 양) 리스트 선언
    2. 특정 i번째에 대해서, i를 마시거나 마시지 않거나에 대하여 가지수를 생각
       i-3   i-2   i-1   i
        O     O     X    O --> dp[i] = dp[i-2] + cup[i]
        O     X     X    O --> 첫번째 가짓수가 더 크므로 제외
        O     X     O    O --> dp[i] = dp[i-3] + cup[i-1] + cup[i]
        O     O     X    X --> 첫번째 가짓수가 더 크므로 제외
        O     X     O    X --> 세번째 가짓수가 더 크므로 제외
        X     O     O    X --> dp[i] = dp[i-1]
    3. 점화식 중 가장 큰 값 찾기
'''
import sys
n = int(input())
cup = [0]
dp = [0] * 10001

for i in range(n):
    cup.append(int(sys.stdin.readline()))    

dp[1] = cup[1]
if n >= 2:
    dp[2] = cup[1] + cup[2]
if n >= 3:
    dp[3] = max(cup[1] + cup[3], cup[2] + cup[3], cup[1]+cup[2])
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(dp[i-3] + cup[i-1] + cup[i], dp[i-2] + cup[i], dp[i-1]) 

print(max(dp))