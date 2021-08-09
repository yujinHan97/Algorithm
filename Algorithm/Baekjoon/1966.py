''' 
    1966 프린터 큐
    알고리즘:
    1. queue에 인덱스와 중요도를 쌍으로 저장해서, 중요도가 젤 높은 걸 항상 찾는다
    2. 중요도가 가장 높은 쌍이 큐의 맨 앞에 있으면 큐에서 빼고, 중요도가 낮으면 뒤로 옮긴다
    3. 큐에서 뺄 때마다 빼는 횟수를 1 증가시키는데, 빼는 수의 인덱스를 M과 비교해서 같으면 종료
'''
from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    pri = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        queue.append([i, pri[i]])

    count = 0
    while queue:
        mostimp = queue[0][1]
        for j in range(1, len(queue)):
            if mostimp < queue[j][1]:
                mostimp = queue[j][1]

        if queue[0][1] == mostimp:
            result = queue.popleft()
            count += 1
            if result[0] == M:
                break
            
        else:
            queue.rotate(-1)

    print(count)