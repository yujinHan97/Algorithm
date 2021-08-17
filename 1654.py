'''
    1654 랜선 자르기
    알고리즘:
    1. 전체 길이에서 랜선을 자르고 남은 길이는 재사용할 수 없기 때문에 전체 길이에서 N개로 나눈 값이 end
    2. start = 1부터 이분 탐색으로 구한다 (맨처음에 틀렸던 이유 : start = 0으로 해서 mid가 0이 되는 경우가 존재)
    3. 이분 탐색한 길이로 잘라서 개수가 N개 이상인 것만 저장을 해서 그 중 길이가 가장 큰 걸 선택
'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())

oh, park = [], []
for _ in range(K):
    oh.append(int(input()))

# 이분 탐색
start, end = 1, sum(oh) // N 
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for length in oh:
        temp += (length // mid) 

    if temp >= N:
        park.append(mid)
        start = mid + 1
    else:
        last = mid - 1
        
park.sort(reverse = True)
print(park[0])
