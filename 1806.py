'''
    1806 부분합
    알고리즘:
    1. start, end의 투포인터를 이용한다
    2. start를 기준으로 end를 이동하면서 S보다 작은경우 end를 계속 움직여서 합을 더한다
    3. 그 합의 인덱스 차를 넣으면 이제 다시 새로운 start를 기준으로 한다
    4. 이 때, 이전의 sum이 S보다 이미 크다면 end를 줄이면서 sum을 조정
'''
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
A = list(map(int, input().split()))

end = 0
sum = 0

index = []
for start in range(N):
    while sum > S and end > start: # start를 옮겼는데도 이미 sum이 S보다 크다면 end를 다시 왼쪽으로 옮겨서 조정
        end -=1
        sum -= A[end]

    while sum < S and end < N: # S보다 작은 경우에 계속 end를 이동
        sum += A[end]
        end += 1

    if sum >= S: # sum이 S 이상인 경우에, index의 차이를 넣어준다
        index.append(end - start)
    sum -= A[start]

if len(index) == 0: # 그런 합을 만들지 못하는 경우
    print(0)
else:
    print(min(index))
