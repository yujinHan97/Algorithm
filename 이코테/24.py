'''
    알고리즘:
    (처음에는 평균이 최소 거리일줄 알았는데 틀렸음 -> 중간값이 최소 거리이다)
    1. 짝수, 홀수 판단하여 중간값을 구하면 된다.
'''
n = int(input())
house = list(map(int, input().split()))
house.sort()


if n % 2 ==0:
  print(house[n//2-1])
else:
  print(house[n//2])
  
