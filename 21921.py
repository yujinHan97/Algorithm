'''
    알고리즘:
    1. 자료의 개수가 클 때, 구간합을 구하려면 누적합 쓰기 
    2. 연속 며칠동안 ==> 투포인터 i, j로 누적합에서 빼서 최댓값 구함
'''
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))
cumm_arr = []
cumm_arr.append(arr[0])
for i in range(1, len(arr)):
    cumm_arr.append(cumm_arr[i-1] + arr[i])

max_visit = []
for i in range(1, len(arr)):
    j = i-X
    if j < 0:
        max_visit.append(cumm_arr[i])
    else:
        max_visit.append(cumm_arr[i] - cumm_arr[j])

if sum(max_visit) == 0:
    print("SAD")
else:
    result = max(max_visit)
    print(result)
    print(max_visit.count(result))
