'''
    2164 카드2
    알고리즘:
    1. deque 사용
    2. 맨 위의 카드를 버릴땐 popleft, 그 다음 카드를 뒤로 옮길땐 rotate
    3. rotate의 매개변수로 음수이면 왼쪽, 양수이면 오른쪽으로 회전
'''
from collections import deque
N = int(input())
queue = deque(i for i in range(1, N+1))

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])