'''
    알고리즘:
    1. 시간 C가 양수가 아닌 음수인 경우도 존재 --> 벨만포드 알고리즘
    (음수가 존재하면 벨만포드로 풀어야함 / 다익스트라는 적용 불가)
'''
import sys

def bellmanford(start):
    dist[start] = 0 # 시작 노드 초기화

    for i in range(N): # 전체 N-1번 반복
        for j in range(M): # 매번 모든 간선 확인
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]

            # 최단 경로가 있는 경우
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost

                # 마지막에도 값이 갱신되면 음수 cycle존재하므로, True 반환
                if i == N-1:
                    return True

    return False

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = []
dist = [INF] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

# 벨만포드 최단 경로 알고리즘 함수 호출
negative_cycle = bellmanford(1)

# 시간을 무한히 오래 전으로 되돌릴 수 있는 경우 (= 음수 사이클 존재), -1을 출력
if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF: # 해당 도시로 가는 경로 없는 경우
            print(-1)
        else:
            print(dist[i])
