'''
    알고리즘:
    1. 회전하는 연산을 최소로 하기 위해서 왼쪽에서 가까운지 오른쪽에서 가까운지 판별해야한다.
    2. 앞에서 부터 그 숫자를 찾고, index를 구하는데, 총 길이의 반보다 작으면 왼쪽으로 회전하면 최소이고, 반보다 크면 오른쪽으로 회전하면 최소이다.
    3. 그래서 왼쪽, 오른쪽으로 회전을 하고 큐에 맨 앞에 pop할 원소가 나타나면 pop하면 된다
'''
from collections import deque

N, M = map(int, input().split())
popindex = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

rotate = 0
while popindex:
    if popindex[0] == queue[0]:
        queue.popleft()
        del popindex[0]
    else:
        index = 0
        for i in range(len(queue)):
            if queue[i] != popindex[0]:
                index += 1
                continue
            else:
                break

        if index > (len(queue) // 2):
            while queue[0] != popindex[0]:
                queue.rotate(1) 
                rotate += 1
        else:
            while queue[0] != popindex[0]:
                queue.rotate(-1) 
                rotate += 1

print(rotate)
