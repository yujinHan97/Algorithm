'''
    알고리즘:
    1. *2, *3, *5를 하는 것을 반복하면 못생긴 수 임을 파악하는 것 까지는 완료
    2. 구현하기 위해서, 가장 작은 거 꺼내고 n번째임을 확인하고 하기 위해서 구현하였더니 시간 초과 같이 kill 되었음. 
    3. 책 풀이를 보고 했다 -> 인덱스, next를 사용하여 매번 *2, 3, 5하고 작은 것을 차례대로 넣는 방법
'''
n = int(input())
ugly = [0] * n
ugly[0] = 1

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
  ugly[i] = min(next2, next3, next5)

  if ugly[i] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[i] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[i] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])
