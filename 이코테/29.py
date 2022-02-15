'''
    알고리즘:
    (어려워서 책 해설 보았지만, 설명이 부족해서 아래 url 참고
    참고한 url : https://tmdrl5779.tistory.com/119)
    1. 반복적으로 gap을 설정 -> gap은 설치할 공유기들 사이의 최소 거리
    2. 각 gap에 대하여, 
      2-1) 설치 가능한 공유기 개수가 c보다 크면 ? gap을 더 키워서 멀찌감치 공유기를 설치
      2-2) 설치 가능한 공유기 개수가 c보다 작으면 ? gap을 더 줄여서 좀 가깝게 공유기를 설치
'''
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))
house.sort()

# 공유기 사이 거리 최솟값과 최댓값
start, end = 1, house[n-1] - house[0]
result = []
 
while start <= end:
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 gap
    current = house[0] # 공유기가 설치된 집의 위치 
    count = 1
    
    for h in house:
      if current + mid <= h: # 현재 + gap과 집을 비교해서 설치 가능하면 공유기 설치
        count += 1
        current = h # 설치한 집으로 current 갱신
     
    # 설치 가능한 공유기 개수(count) 와 c값을 비교하여 gap 조정
    if count >= c:
      start = mid + 1 
      result.append(mid) # 가능한 거리들을 result 리스트에 저장
    else:
      end = mid - 1 
 
print(max(result))
