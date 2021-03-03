'''
    10845 큐
    알고리즘:
    1. 리스트를 사용해서 구현
    2. pop을 할 때, pop(0)을 하면 앞에서부터 제거한다
'''
import sys
N = int(input())
queue = []

for i in range(N):
    op = sys.stdin.readline().strip()

    if ' ' in op:
        op, num = op.split()
        num = int(num)

    if op == "push":
        queue.append(num)
    elif op == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif op == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif op == "size":
        print(len(queue))
    elif op == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif op == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)