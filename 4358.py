'''
    4358 생태학
    알고리즘:
    1. tree종류를 key로 하는 dict를 생성해서 ratio 구하면 된다.
    (defaultdict 활용해 보자!)
'''
# defaultdict 사용한 코드
import sys
from collections import defaultdict
input = sys.stdin.readline

# defaultdict의 매개변수로 int, list, set이 가능하고, int일때는 0/list,set일 때는 각각 빈 자료구조가 디폴트
tree = defaultdict(int)
count = 0

while True:
    spec = input().rstrip()
    
    if not spec:
        break

    tree[spec] += 1 # defaultdict를 0으로 설정했으니까 입력받을때 마다 1씩 증가시켜주면 된다
    count += 1

tree_list = list(tree.keys())
tree_list.sort()

for i in range(len(tree_list)):
    ratio = tree[tree_list[i]] / count * 100
    print('%s %.4f' %(tree_list[i], ratio))

# 그냥 코드
#import sys
#input = sys.stdin.readline

#tree = {}
#count = 0
#while True:
#    spec = input().rstrip()
    
#    if not spec:
#        break

#    if spec in tree:
#        tree[spec] += 1
#    else:
#        tree[spec] = 1

#    count += 1

#tree_list = list(tree.keys())
#tree_list.sort()

#for i in range(len(tree_list)):
#    ratio = tree[tree_list[i]] / count * 100
#    print('%s %.4f' %(tree_list[i], ratio))
