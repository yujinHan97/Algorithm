'''
    알고리즘:
    (다음에 다시 풀기)
    1. ICN을 시작으로 dfs 수행
    2. dfs를 수행하면서, 모든 티켓들을 다 사용할 때까지 계속 dfs
    3. 모든 티켓을 다 사용했을 때 -> 경로의 마지막 부분
    4. 따라서, 경로를 answer에다 집어넣으면서 dfs 갔던거 return
    5. 결국 answer는 경로의 역순이 되어있으니까 [::-1]로 다시 역순 반환
'''
from collections import defaultdict

def solution(tickets):
    answer = []

    # key 에러 나지 않도록 defaultdict로 생성
    routes = defaultdict(list)
    # ticket을 일단 그래프 형식으로 생성 (dict 자료형)
    for a, b in tickets:
        routes[a].append(b)
    for key in routes.keys():
        routes[key].sort() # 알파벳 순으로 앞선다고 했으니

    def dfs(start):
        while routes[start]:
            dfs(routes[start].pop(0))
        
        if not routes[start]:
            answer.append(start)
            return 
        
    dfs("ICN")
    return answer[::-1]
