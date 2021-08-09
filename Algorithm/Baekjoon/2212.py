'''
    2212 센서
    알고리즘
    1. 센서 N개를 K개로 분류한다 (그러면 기준은 K-1개가 된다)
    2. 차이 중에서 제일 큰 K-1개가 기준이 되므로, 그걸 빼고 남은 것들의 합을 구하면 된다
'''
import sys

N = int(input())
K = int(input())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

# 예외처리) 집중국 개수가 센서 개수 이상이면, 센서 개수마다 세우면 되니까, 길이의 최솟값은 0
if K >= N: 
    print(0)
    exit()

diff = []
for i in range(1, N): # 센서끼리의 간격을 저장
    diff.append(sensor[i] - sensor[i-1])
diff.sort()

for _ in range(K-1):
    diff.pop()

print(sum(diff))