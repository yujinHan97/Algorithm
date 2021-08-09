'''
    1991 트리 순회
    알고리즘:
    1. 트리 딕셔너리를 생성해서, key로는 노드 값, item으로는 (left, right)의 값으로 저장
    2. 전위, 중위, 후위 순회 메소드 생성, 재귀 호출
'''
def pre_order(node):
    print(node, end = '')
    if tree[node][0] != '.':
        pre_order(tree[node][0])
    if tree[node][1] != '.':
        pre_order(tree[node][1])

def in_order(node):
    if tree[node][0] != '.':
        in_order(tree[node][0])
    print(node, end = '')
    if tree[node][1] != '.':
        in_order(tree[node][1])

def post_order(node):
    if tree[node][0] != '.':
        post_order(tree[node][0])
    if tree[node][1] != '.':
        post_order(tree[node][1])
    print(node, end = '')

N = int(input())
tree = {}
for i in range(N):
    node, left, right = map(str, input().split())
    tree[node] = (left, right) # 트리 딕셔너리에 left, right의 튜플 형태로 삽입

#print(tree)
# 전위, 중위, 후위 순회 실행
pre_order('A')
print()
in_order('A')
print()
post_order('A')
