'''
    알고리즘:
    1. 맵의 최단거리 => BFS 사용
    2. 내 캐릭터에서 출발해서 상대방 캐릭터까지 최단거리 구하면 된다
    3. 단, 끝까지 갓는데 1인 경우는 => 도달 할 수 없다는 의미
'''
from collections import deque
def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0, 0))
        
    while q:
        x, y = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1                      
                    q.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1] 
        
    return answer
