'''
    https://level.goorm.io/exam/49112/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0/quiz/1
    알고리즘:
    1. 현재 내가 가려고 하는 칸과 -1, -2, -3 칸 중에서 가장 적은 오염이 될 수 있는 걸 골라서 가기 -> dp
'''
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n)
if n > 3:
  for i in range(3):
    dp[i] = arr[i]
  for i in range(3, len(arr)):
    dp[i] = min(dp[i-3], dp[i-2], dp[i-1]) + arr[i]

  answer = min(dp[n-1], dp[n-2], dp[n-3])
else:
	answer = min(arr[0:3])
	
print(answer)
