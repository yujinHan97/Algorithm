'''
    알고리즘:
    1. sum이 오래걸리는 듯해서 누적합을 이용해서 풀음
'''
import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    N, L = map(int, input().split())
    costs = list(map(int, input().split()))

    min_cost = 1e9
    # 누적 합 리스트 
    accum = [0] * (N+1)
    for i in range(len(costs)):
        accum[i+1] = accum[i] + costs[i]

    for start in range(1, N-L+2):
        for last in range(start+L-1, N+1):
            min_cost = min(min_cost, (accum[last]-accum[start-1])/(last-start+1))
    
    print("{:.11f}".format(min_cost))
