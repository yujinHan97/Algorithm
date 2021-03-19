'''
    1080 행렬
    알고리즘:
    1. 매 행과 열의 원소마다 비교를 하면서, 수가 다르다면, 그 수를 기준으로 3*3을 반전시킨다
    2. 반전할 때 마다 횟수를 +1 하고, 과정 1을 반복한다
    3. 처음부터 끝까지 다 비교를 완료했으면, A와 B를 비교하고, 같다면 count 수 출력
    4. 다르다면, -1 출력
'''
import sys
def reverse(x, y, arr): # 3*3의 크기에 대하여, 0-->1, 1-->0 으로 반전시키기
    for a in range(x, x+3):
        for b in range(y, y+3):
            arr[a][b] = 1 - arr[a][b]

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().strip())))
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().strip())))

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]: # A원소가 B의 원소와 다른 경우, 그 값을 기준으로 3*3 reverse
            reverse(i, j, A)
            count += 1

# 행렬 비교, 반전 완료 후 A와 B행렬 비교
isEqual = True
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]: #행렬에서 원소가 1개라도 다른 경우, False
            isEqual = False 

if isEqual == True:
    print(count)
else:
    print(-1)