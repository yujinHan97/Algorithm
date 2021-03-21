'''
    11497 통나무 건너뛰기
    알고리즘:
    (풀지 못하고 구글링 해 본 문제)
    1. 먼저 통나무를 정렬한다
    2. 가장 작은 2개를 양끝으로 배치하는 걸 반복
    3. 그러면, 인접한 수의 인덱스 차이는 2가 된다
    4. 이 차이들 중에서 가장 큰 값을 출력
'''
import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    
    L.sort()
    ans = 0
    for i in range(2, N):
        diff = L[i] - L[i-2]
        ans = max(ans, diff)

    print(ans)