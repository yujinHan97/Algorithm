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
    
---------------------------------------------------------------------------------------------------------
'''
    알고리즘: (직접 풀어서 맞춤 - 50분)
    1. 2차원 세계의 블록을 graph로 만들어서 블록을 1로 초기화 
    2. graph의 모든 칸 마다 0이면, 해당 col 기준으로 왼쪽 오른쪽에 1이 모두 있으면 빗물이 고일 수 있음
'''
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

graph = [[0] * w for _ in range(h)]
for i in range(len(heights)):
  for j in range(heights[i]):
    graph[h-j-1][i] = 1

answer = 0
for i in range(h):
  for j in range(w):
    if j == 0 or j == w-1: # 가장 끝 칸들은 어차피 빗물이 고일 수 없으니까 제외
      continue
    if graph[i][j] == 0:
      # 왼쪽과 오른쪽 모두 1이 있으면 == 블록이 양옆에 있으므로 빗물이 싸일 수 있음
      if graph[i][:j].count(1) != 0 and graph[i][j+1:].count(1) != 0:
        graph[i][j] = 2 # 빗물을 2로 표시 후, answer 증가
        answer += 1
        
print(answer)
