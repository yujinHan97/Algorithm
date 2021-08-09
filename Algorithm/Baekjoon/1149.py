'''
    1149 RGB거리
    알고리즘:
    1. 두번째 집부터 색깔을 정한다. 
    2. 비용이 최소가 되려면, 한단계 전 집에서 다른 색들 중 최소인 집을 선택한다
    3. 최소인 집 비용과 자기 집 비용을 더해서 계속 집 값을 갱신하고 최소값 찾기
'''

import sys
N = int(input())
cost = []

for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    # i번째에 빨간 집을 골랐으면, 그 전 단계에서 파란색, 초록색 집 중에서 적은 가격을 선택하고, 현재 단계에서 자기 빨간색 가격을 더하기
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    # i번째에 초록 집을 골랐으면, 그 전 단계에서 파란색, 빨간색 집 중에서 적은 가격을 선택하고, 현재 단계에서 자기 초록색 가격을 더하기
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    # i번째에 파랑 집을 골랐으면, 그 전 단계에서 빨간색, 초록색 집 중에서 적은 가격을 선택하고, 현재 단계에서 자기 파란색 가격을 더하기
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[N-1]))