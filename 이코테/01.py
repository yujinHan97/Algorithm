'''
    알고리즘:
    (다시 풀기 => 알고리즘 생각은 했으나 구현 못했음)
    1. 여행을 떠날 수 있는 그룹 수의 최댓값 -> 각 그룹에 있는 사람이 적을수록 그룹 수가 최대가 될 수 있음.
    2. 1번에 의해서, 오름차순 정렬
    3. (참고한 부분) '현재 그룹에 포함된 사람 수 >= 현재 확인하고 있는 사람의 공포도' 인 경우 그룹 설정
''' 
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

people, group = 0, 0
for i in arr:
  people += 1

  if people >= i:
    group += 1
    people = 0

print(group)
