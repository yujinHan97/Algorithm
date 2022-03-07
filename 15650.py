'''
    알고리즘:
    1. combinations 라이브러리 사용해서 조합 구함
    2. 하나의 iterable을 공백 포함하여 출력하기 위해서 * 사용
'''
from itertools import combinations

arr = []
n, m = map(int, input().split())
for i in range(n):
  arr.append(i+1)

combination = list(combinations(arr, m))
for comb in combination:
  print(*comb)
