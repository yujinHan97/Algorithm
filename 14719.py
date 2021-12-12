'''
    알고리즘:
    (나중에 다시 풀기)
    1. 현재 블록의 양 끝에 높은 블록이 있다면, 그중 min과의 차이점만큼 물이 고일 수 있음
    2. 양 끝 = 오른쪽 중 최대, 왼쪽 중 최대
'''
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
count = 0

for i in range(1, W-1):
    left = max(blocks[:i]) # 현재 블록보다 왼쪽 중에서 최대
    right = max(blocks[i+1:]) # 현재 블록보다 오른쪽 중에서 최대
    poss = min(left, right) # 그 중 작은 것 만큼만 물이 고일 수 있음
    
    if poss - blocks[i] > 0: # 만약 가장 큰 블록같은 경우에, -가 될 수 있어서 
        count += (poss - blocks[i])
    
print(count)
    
