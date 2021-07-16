'''
    1764 듣보잡
    알고리즘:
    1. N과 M이 각각 50만 이하이므로, N^2인 경우에는 2500억 --> 시간초과
    2. 따라서, 이분탐색으로 푼다
    3. 이분탐색을 위해서는 반드시 정렬을 해야한다
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [] # 듣도 못한 사람
b = [] # 보도 못한 사람
for _ in range(N):
    a.append(input().strip())
for _ in range(M):
    b.append(input().strip())
b.sort()

c = [] # 듣보
for person in a:
    start, end = 0, len(b)-1
    while start <= end:
        mid = (start + end) // 2

        if b[mid] == person:
            c.append(person)
            break
        elif b[mid] < person:
            start = mid + 1
        else:
            end = mid -1  

print(len(c))
c.sort()
for person in c:
    print(person)
