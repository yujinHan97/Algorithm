''' 
    13305 주유소
    알고리즘: 
    1. 도시와 도시의 주유 가격을 쌍으로 딕셔너리를 생성하고, 주유 가격을 기준으로 오름차순 정렬한다
    2. 주유 가격이 싼 것부터 차례대로 도시를 골라서, 그 도시부터 오른쪽 끝까지 갈 양 만큼 주유 한다
    3. 그 거리만큼 ddict에서 다 빼주면 된다
    이 풀이는 그러나 시간초과 
    
    정답 풀이:
    1. 주유 가격의 처음값을 최솟값으로 저장하고, 도시를 이동할때마다 최솟값을 찾아가면서 가격을 최소로 한다.
    2. 처음 도시에서는 그 가격이 싸든 비싸든 무조건 거리만큼은 넣어야한다.
    3. 다음 도시부터는 그 도시의 가격이 현재의 최소값과 비교해서 최소값보다 작으면 최솟값으로 설정해서 거리만큼 이동
    4. 비교했는데 최소값보다 크면, 최솟값으로 그 도시의 거리만큼 이동
'''

import sys
N = int(input())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
del price[N-1] # 마지막 도시에서의 가격은 필요가 없는 값이므로 삭제 

total = price[0] * dist[0] 
minp = price[0]

for i in range(1, N-1):
    minp = min(minp, price[i])
    total += (dist[i] * minp)
   
print(total)