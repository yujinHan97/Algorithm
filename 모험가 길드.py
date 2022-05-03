'''
    정답!
    알고리즘:
    1. 그룹 수를 최대로 해야하니까, 공포도가 낮은 애들부터 그룹을 형성하도록 -> 오름차순 정렬
    2. 각 공포도에 대하여, 모험가를 한 명씩 넣는데 이 때 공포도 이상이면 그룹을 형성 -> group += 1, count = 0으로 해서 그룹 형성하고 또 다른 새로운 그룹을 위한 모험가 수를 0으로 초기화
'''
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
group, count = 0, 0
for g in arr:
  count += 1

  if count >= g:
    group += 1
    count = 0

print(group)
