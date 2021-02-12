'''
    15649 N과 M(1)
    알고리즘 :
    1. N개 중에 M개를 순서를 고려해서 뽑는 순열의 알고리즘을 이용
    2. itertools의 permutation을 이용
'''
from itertools import permutations
    
N, M = map(int, input().split())
num_list = []

for i in range(N):
    num_list.append(i+1)

permute = list(permutations(num_list, M))

for i in range(len(permute)):
    for j in range(M):
        print(permute[i][j], end = ' ')
    print()