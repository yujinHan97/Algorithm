'''
    알고리즘:
    1. 최빈값 -> Counter의 most_common() 메소드 사용
    2. most_common(k)를 사용하여 상위 k개 데이터 추출 후, [0][0]으로 최빈값 출력
'''
from collections import Counter

arr = []
for _ in range(10):
  arr.append(int(input()))

print(sum(arr)//10)
print(Counter(arr).most_common(1)[0][0])
