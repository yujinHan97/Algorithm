'''
    2667 단지 번호 붙이기
    알고리즘:
    1. 상하좌우로 움직이면서 덩어리가 생길때 True를 반환하면 result +1
    2. 집을 방문하면서 1 --> 0으로 바뀔때마다 count수를 증가시켜준다
'''
import sys
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

n = int(input())
graph = []
countings = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

result = 0
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j) == True:
            result += 1
            countings.append(count)

print(result)
countings.sort()
for i in countings:
    print(i)
