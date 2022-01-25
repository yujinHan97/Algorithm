'''
    알고리즘:
    (어려웠던 문제, 아직도 이해가 조금은 잘 안간다)
    1. 1부터 만들수 있는 값인지 체크한다
    2. coins를 정렬해 놓고, 1부터 만들 수 있다면 해당 coin만큼 target을 올리면 된다 
       (왜냐면, 해당 코인만큼 더하면 그 전까지는 다 만들 수 있는 금액이기 때문)
'''
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
  if target >= coin:
    target += coin
  else:
    break

print(target)
