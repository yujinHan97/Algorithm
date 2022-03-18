'''
    알고리즘:
    1. 모든 섬을 연결하면서 가장 최소의 비용? -> 크루스칼 알고리즘
'''
def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
            
        return parent[x]
    
    def union_parent(a, b, parent):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
           
    for cost in costs:
        from_, to_, c = cost
        if find_parent(parent, from_) != find_parent(parent, to_):
            union_parent(from_, to_, parent)
            answer += c
    
    return answer
