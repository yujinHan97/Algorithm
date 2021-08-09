'''
    15651 N과 M(3)
    알고리즘 :
    1. N개 중에 중복을 허용해서 M개를 순서를 고려해서 뽑는 중복순열의 알고리즘을 이용
    2. itertools의 product를 이용
'''
from itertools import product

N, M = map(int, input().split())
num_list = []

for i in range(N):
    num_list.append(i+1)

a = list(product(num_list, repeat = M))

for i in range(len(a)):
    for j in range(M):
        print(a[i][j], end = ' ')
    print()