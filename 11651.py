import sys

N = int(input())
coord = []
for i in range(N):
    coord.append(list(map(int, sys.stdin.readline().split())))

coord.sort(key = lambda x:(x[1], x[0]))

for i in coord:
    print(i[0], i[1])
