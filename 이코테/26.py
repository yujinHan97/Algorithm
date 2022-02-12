'''
    알고리즘:
    1. 각각 작은 수의 카드 묶음을 합쳤을 때, 최적의 해를 보장
    2. 따라서, 매번 카드를 합칠 때마다 정렬하고 작은 카드 묶음 2개를 선택하는 것을 반복하기 위해서 힙 자료구조를 사용
'''
import heapq

n = int(input())
cards = []
for i in range(n):
  cards.append(int(input()))

heapq.heapify(cards)
total = 0
while len(cards) > 1:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  total += a
  total += b
  c = a + b
  heapq.heappush(cards, c)

print(total)
