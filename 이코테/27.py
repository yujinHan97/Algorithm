'''
    알고리즘:
    1. bisect 라이브러리를 이용해서 구현
       - bisect_left : target 숫자가 리스트에 이미 있으면 가장 왼쪽(앞)의 위치를 반환
       - bisect_right : target 숫자가 리스트에 이미 있으면 가장 오른쪽(뒤)의 위치를 반환
'''
import bisect

n, x = map(int, input().split())
nums = list(map(int, input().split()))

first = bisect.bisect_left(nums, x)
last = bisect.bisect_right(nums, x)

if last - first == 0:
  print(-1)
else:
  print(last-first)
  
  
