'''
    알고리즘:
    1. 재귀를 이용해서 모든 경우의 수 출력
'''
def solution():
    if len(arr) == N:
        print(*arr)
        return

    for i in range(1, N+1):
        if i not in arr: 
            arr.append(i)
            solution()
            arr.pop() 

N = int(input())
arr = []
solution()
