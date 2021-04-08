'''
    11728 배열 합치기
    알고리즘:
    1. 이미 정렬된 배열 두개를 비교하는 것이기 때문에 앞의 인덱스부터 비교
    2. A의 index를 가리키는 l 포인터와 B의 index를 가리키는 r포인터를 비교하면서
       - A[l] <= B[r], 새로운 리스트에 A의 요소를 넣고 A의 포인터 이동
       - A[l] > B[r], 새로운 리스트에 B의 요소를 넣고 B의 포인터 이동
    3. A를 이미 다 넣은 상태라면(=> l == N), B의 요소들을 쭉 새로운 리스트에 넣기
    4. B를 이미 다 넣은 상태라면(=> r == M), A의 요소들을 쭉 새로운 리스트에 넣기
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = r = 0 # l은 A의 pointer, r은 B의 pointer
arr = []
while l < N and r <M :
    if A[l] <= B[r]: # A가 작으니까 새로운 리스트에 A의 요소를 넣고 A의 포인터 이동
        arr.append(A[l])
        l += 1

    elif A[l] > B[r]: # B가 작으니까 새로운 리스트에 B의 요소를 넣고 B의 포인터 이동
        arr.append(B[r])
        r += 1

if l == N: # A를 다 넣었다면, l의 포인터가 끝까지 갔을 테니까 B를 다 넣기
    for i in range(r, M):
        arr.append(B[i])
elif r == M: # B를 다 넣었다면, r의 포인터가 끝까지 갔을 테니까 A를 다 넣기
    for i in range(l, N):
        arr.append(A[i])

for num in arr:
    print(num, end = ' ')
