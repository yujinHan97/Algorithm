'''    
    알고리즘:
    (잘 모르겠어서, 해설 참조)
    1. '증가하는 부분 수열' 알고리즘을 참고하여 풀기 위해서 reverse() 시켰다
        (우리는 감소하는 걸 찾아야 하는데, 알고리즘은 증가하는 걸 사용하기 때문)
    2. dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이를 나타냄
'''
n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n
soldiers.reverse()

for i in range(1, n):
  for j in range(0, i):
    if soldiers[i] > soldiers[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
