'''
    알고리즘:
    1. 두 개의 포인터 사용
    2. 두 개의 포인터가 가리키는 용액의 특성 값을 더해서, 
       - 양의 값이면, 더 줄여야 하니까 +의 값을 작은 값을 가리키도록 --> right -= 1
       - 음의 값이면, 더 키워야 하니까 -의 값을 작은 값을 가리키도록 --> left += 1
    3. 용액 특성값의 합이 최소값이어서 갱신이 되는 경우에, 두 개의 특성값 a, b에 할당
'''
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
liq = list(map(int, input().split()))
liq.sort()

# 두 개의 포인터 생성
left = 0 
right = N-1
answer = INF

while left < right:
    tmp = liq[left] + liq[right]

    # 두개의 포인터가 가리키는 합의 절댓값이 더 작은 경우(= 0에 가까운 경우)
    if abs(tmp) < answer: 
        a = liq[left]
        b = liq[right]
        answer = abs(tmp) # 용액 특성값 할당하고, answer 갱신

    if tmp >= 0:
        right -=1
    else:
        left += 1
        
print(a, b)
