'''
    2847 게임을 만든 동준이
'''
import sys

N = int(input())
level = []
count = 0
next = []

for i in range(N):
    level.append(int(input()))
    next.append(level[i])

for i in range(N-1):
    del next[0]
    minv = min(next)
       
    if level[i] >= minv:
        diff = level[i] - minv + 1
        count += diff
        level[i] -= diff

for i in range(N-2, -1, -1):
    while level[i] >= level[i+1]:
        level[i] -=1 
        count += 1

print(count)