'''
    1300 K번째 수
    알고리즘:
    (for문을 2번 돌려서, 리스트 만들고 정렬 --> 메모리 초과)
    1. 아주 대충 이해했다. https://claude-u.tistory.com/449 참고 
    2. 어떤 임의의 숫자 mid보다 작은 숫자가 몇개인지 알면, mid가 몇번째 숫자인지 알 수 있다
    3. 각 행마다, mid보다 작은 숫자의 개수를 찾기
       1행 ==> min(mid//1, N)
       2행 ==> min(mid//2, N)
       ...
    4. 개수와 K를 비교해서, 
       - 개수가 더 많은 경우 범위를 좁히면 되니까 end = mid - 1
       - 개수가 적거나 같은 경우 그 mid 값을 저장하고, start = mid + 1
'''
import sys
N = int(input())
K = int(input())

start, end = 1, K # K번째 숫자는 절대 K보다 클 수 없다
answer = 0
while start <= end:
    mid = (start+end) // 2

    count = 0
    for i in range(1, N+1):
        count += min(mid//i, N)

    if count < K:
        start = mid +1 
    else:
        answer = mid
        end = mid - 1

print(answer)
