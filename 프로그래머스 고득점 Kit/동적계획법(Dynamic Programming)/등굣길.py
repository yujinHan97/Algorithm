'''
    알고리즘:
    (초딩때 풀었던 최단경로 개수 구하는 방법으로 풀었다)
    1. i == 0인 곳은 왼쪽에서 오는 경우 1가지이므로, [i][j-1] 값 그대로
    2. j == 0인 곳은 위쪽에서 오는 경우 1가지이므로, [i-1][j] 값 그대로
    3. 그 외의 경우에는 왼쪽과 위쪽에서 오는 경우의 수를 더하면 최단경로의 경우의 수이다
'''
def solution(m, n, puddles):
    answer = 0
    
    graph = [[1] * (m) for _ in range(n)]
    for puddle in puddles:
        a, b = puddle
        graph[b-1][a-1] = 0
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue    
                
            if i == 0 and j == 0:
                continue
            elif i == 0:
                graph[i][j] = graph[i][j-1] % 1000000007
            elif j == 0:
                graph[i][j] = graph[i-1][j] % 1000000007
            else: 
                graph[i][j] = (graph[i][j-1] + graph[i-1][j]) % 1000000007
                
    return graph[n-1][m-1]
