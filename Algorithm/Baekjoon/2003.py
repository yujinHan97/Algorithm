'''
    2003 수들의 합2
    알고리즘:
    1. 투 포인터를 이용하면, 연속 구간합을 O(N)안에 찾을 수 있다
    2. start를 기준으로 end를 가능한만큼 오른쪽으로 옮겨가면서 합이 같으면 경우의 수 증가
    3. 가능한 합을 찾았으면, 또 다른 경우를 찾기 위해 start를 옮기고 sum에서 start가 가리키는 수 빼기
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

end = 0 # 두개의 포인터 중 하나를 나타내는 변수
sum = 0 # 두개의 포인터가 가리키는 구간의 합을 나타내는 변수
count = 0 # 구간의 합이 M이 되는 경우의 수를 나타내는 변수

for start in range(N):
    while sum < M and end < N: # end를 가능한 만큼 오른쪽으로 이동
        sum += A[end] # 이동하는 수를 항상 더한다
        end += 1

    if sum == M: # 어떤 구간의 합이 M이라면, 경우의 수 +1 
        count += 1

    sum -= A[start] # 구간의 첫번째 요소를 옮기고, 이전 첫번째 요소는 뺀다

print(count)
