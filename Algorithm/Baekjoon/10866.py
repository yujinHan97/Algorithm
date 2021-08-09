'''
    10866 덱
    알고리즘:
    1. 리스트를 사용해서 구현
    2. pop을 할 때, pop(0)을 하면 앞에서부터 제거한다
'''
import sys
N = int(input())
queue = []

for i in range(N):
    op = sys.stdin.readline().split()

    if op[0] == "push_front":
        queue.insert(0, op[1])
    elif op[0] == "push_back":
        queue.append(op[1])
    elif op[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif op[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif op[0] == "size":
        print(len(queue))
    elif op[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif op[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])