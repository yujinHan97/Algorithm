'''
    1931 회의실 배정
    알고리즘: 
    1. 끝나는 시간 먼저, 그리고 시작시간을 기준으로 list를 정렬한다. 
    2. 제일 첫번째 회의를 고르고, 그 끝나는 시간이후에 있는 것중에 가장 앞에 있는 회의를 고르는 것 반복
'''
import sys
N = int(input())
conv = []
for i in range(N):
    conv.append(list(map(int, sys.stdin.readline().split())))

conv.sort(key = lambda x:(x[1], x[0]))

count = 1
i = 0
while i < (len(conv) - 1):
    start = conv[i][0]
    end = conv[i][1]
    
    for y in range(i+1, len(conv)):
        i += 1
        if conv[y][0] >= end:
            count+= 1
            break

print(count)