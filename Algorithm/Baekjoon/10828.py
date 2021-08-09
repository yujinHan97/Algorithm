'''
    10828 스택
    알고리즘:
    1. list이용
'''
import sys

def push(a):
    stack.append(a)

def pop():
    if len(stack) == 0:
        print(-1)
    else: print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else: print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])

N = int(input())
stack = []

for i in range(N):
    s = sys.stdin.readline().split()
    op = s[0]

    if op == 'push':
        num = s[1]
        push(num)
    elif op == 'pop':
        pop()
    elif op == 'size':
        size()
    elif op == 'empty':
        empty()
    elif op == 'top':
        top()