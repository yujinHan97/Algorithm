'''
    (다시풀기)
    알고리즘:
    1. 모든 조합을 다 구한다음에 유일성 --> 최소성 순서로 만족시키는 것 찾기
    2. 최소성에서 &, 유일성에서 tuple 사용법 다시 공부 
'''
from itertools import combinations 
def solution(relation):
    answer = 0
    combi = []
    
    row = len(relation)
    col = len(relation[0])
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    # 유일성 
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if(len(set(tmp)) == row):
            unique.append(i)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)
