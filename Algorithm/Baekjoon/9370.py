'''
    9370 미확인 도착지
    알고리즘:
    (구글링해서 풀었다. 나중에 다시 풀어보기)
    1. start로 시작해서 가는 최단 경로 -- 1
       g에서 시작해서 가는 최단 경로 ---- 2
       h에서 시작해서 가는 최단 경로 ---- 3
    2. 1-2-3 과 1-3-2의 최솟값이 1의 값과 같으면 g,h를 지나온 것이므로 결과에 넣는다
       result1 = start --> g --> h --> end
       result2 = start --> h --> g --> end
       이 두개의 결과 중 최솟값을 start --> end와 비교한다
       값이 같다면 answer에 저장
'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dajikstra(start):
    q = []
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

t = int(input())
for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ends = []
    for _ in range(t):
        ends.append(int(input()))

    from_start = dajikstra(s)
    from_g = dajikstra(g)
    from_h = dajikstra(h)

    answer = []
    for end in ends:
        # start --> g --> h --> end
        result1 = from_start[g] + from_g[h] + from_h[end]
        # start --> h --> g --> end
        result2 = from_start[h] + from_h[g] + from_g[end]

        result3 = min(result1, result2)
        
        # start --> end
        result = from_start[end]

        if result3 == result: # 값이 같다면, g와 h를 지나온 것이므로 answer에 넣기 
            answer.append(end)

    answer.sort()
    for i in answer:
        print(i, end = ' ')

    print()
