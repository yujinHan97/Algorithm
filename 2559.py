'''
    2559 수열
    알고리즘:
    1. 누적합을 구해서 구간의 합을 구한다 
    2. 투포인터를 이용하면서, left를 기준으로 right를 k만큼 떨어진 곳에 할당
    3. 누적합을 구하기 위해서 right - left 를 이용하고, 최대값 출력
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temper = list(map(int, input().split()))

# 온도의 누적합 구하기
accum = []
accum.append(temper[0])
for i in range(1, N):
    sum = accum[i-1] + temper[i]
    accum.append(sum)

arr = []
for left in range(N-K+1):
    right = left + K

    if left == 0: # left가 처음인 경우에는, 그냥 right-1가 누적합
        arr.append(accum[right -1])
    else: # 그 외에는 right-1까지의 누적합에서 left-1까지의 누적합 빼기
        arr.append(accum[right-1] - accum[left-1])

print(max(arr)) # 구간의 누적합 중 최댓값 출력
