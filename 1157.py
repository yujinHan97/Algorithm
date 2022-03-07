'''
    알고리즘:
    1. 단어의 빈도수 -> Counter 사용
    2. 빈도수가 많은게 2개? -> most_common(2)로 해서 앞, 뒤가 똑같은 빈도수인지 판단
'''
from collections import Counter

s = input().upper()
counter = Counter(s).most_common(2)

if len(counter) == 1:
  print(counter[0][0])
else:
  if counter[0][1] == counter[1][1]:
    print("?")
  else:
    print(counter[0][0])
