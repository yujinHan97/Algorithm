'''
    알고리즘:
    1. 서로 연결된 컴퓨터들을 그룹화, 서로 다른 그룹의 개수 찾기? => 서로소 집합 떠올림
    2. 서로소 집합이므로 union-find 알고리즘 구현
    3. 마지막으로, find함수 한 번씩 호출하면서 경로 최적화하기!
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, computers):
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
        
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent, i+1, j+1)
    
    # find 함수를 한 번씩 호출하면서, 경로 최적화하기 => 이것 때문에 TC 1개 계속 틀렸음.
    for i in range(1, n+1):
        find_parent(parent, i)
    
    return len(set(parent[1:]))
