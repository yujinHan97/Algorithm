'''
    알고리즘:
    (맨 처음에는 그냥 '구현'으로 풀었음 -> 시간초과)
    (구글링으로 BFS 풀이 참고하여 풀었다 => 다시 풀기)
    1. 모든 칸에서 주사위로 갈 수 있는 칸으로 갈 때, 최소 횟수를 갱신
    2. 사다리와 뱀의 입력값을 graph에 저장해서, 해당 칸에 도착하는 걸로 지정
    3. visited 리스트로 최단거리 저장
'''
# BFS로 푸는 방법 
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [i for i in range(101)]

# 사다리
for _ in range(n):
  x, y = map(int, input().split())
  graph[x] = y
# 뱀
for _ in range(m):
  u, v = map(int, input().split())
  graph[u] = v
visited = [0 for _ in range(101)] # 최단거리를 저장할 리스트

def bfs():
  q = deque()
  q.append(1)
  visited[1] = 1

  while q:
    x = q.popleft()
    for i in range(1, 7):
      nx = x + i
      if nx > 100:
        continue

      now = graph[nx]
      if visited[now] == 0:
        visited[now] = visited[x] + 1
        q.append(now)

        if now == 100:
          return
          
bfs()
# 1번 칸에서 카운트한 주사위 던진 횟수 1을 빼줌
print(visited[100]-1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 시간 초과 받은 풀이 (입출력 예시 2개는 모두 맞게 나옴, 반례들까지 맞는지는 모름)
# n, m = map(int, input().split())
# ladder, snake = [], []
# now = 1

# for _ in range(n):
#   x, y = map(int, input().split())
#   ladder.append((x, y))
# for _ in range(m):
#   u, v = map(int, input().split())
#   snake.append((u, v))

# ladder.sort(key = lambda x:x[0])
# snake.sort(key = lambda x:x[0])

# count = 0
# while now <= 100:
#   min_temp = now + 1
#   max_temp = now + 6

#   while snake:
#     sna = snake[0]
#     # 현재보다 이전 경로에 snake 있는 건 모두 필요 없으니 삭제
#     if sna[0] < min_temp: 
#       snake.remove(sna)
#     # 현재 경로에서 주사위로 갈 수 있는 경로에 snake가 있는 경우, 6부터 갈 수 있는 최대 칸 수를 구한다 
#     elif min_temp <= sna[0] and sna[0] <= max_temp:
#       for i in range(6, 0, -1):
#         if now + i == sna[0]:
#           continue
#         else:
#           move = i 
#           break
#       now += move
#       break
#     # 주사위로 갈 수 없는 경로에 snake가 있는 경우는 무시
#     else:
#       break

#   while ladder:
#     lad = ladder[0]
    
#     if lad[0] < min_temp:
#       ladder.remove(lad)
#     elif min_temp <= lad[0] and lad[0] <= max_temp:
#       if now < lad[1]:
#         now = lad[1]
#         ladder.remove(lad)
#         continue
#     else:
#       break

#   now = now + 6
#   count += 1

# print(count + 1)

