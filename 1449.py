'''
    1449 수리공 항승
    알고리즘:
    1. 물이 새는 곳을 입력 받고, 정렬을 한다
    2. 차례대로 물이 새는 지점에서 0.5빼고 테이프를 붙인다고 가정할때, 그 다음 지점이 테이프를 붙인 곳 안에 있으면 안붙여도 되고
       그 다음 지점이 테이프를 붙인 곳 밖에 있으면 새로운 테이프를 붙여야 한다
    3. 그래서 테이프를 붙일 때 마다 start, end를 갱신하면서 비교한다  
'''
import sys
N, L = map(int, input().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort()

count = 1
start = leak[0] - 0.5
end = start + L

for i in range(1, N):
    if end > leak[i]:
        continue
    
    start = leak[i] - 0.5
    end = start + L
    count += 1  
    
print(count)