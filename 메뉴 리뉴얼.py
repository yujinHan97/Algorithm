'''
    알고리즘:
    (구현하지 못해서 인터넷 참고 하였음. 다시 풀기)
    1. course의 음식 메뉴마다 모든 조합을 구한다 (중복없도록 하기 위해 정렬 먼저)
    2. 2를 넘는 가장 큰 값에 대해서 메뉴 조합을 생성
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for k in course:
        combs = []
        for order in orders:
            combi = combinations(sorted(order), k)
            combs += combi
        
        count = Counter(combs)
        
        if count:
            max_c = max(list(count.values()))
            
            if max_c >= 2:
                for key, value in count.items():
                    if count[key] == max_c:
                        answer.append(''.join(key))

    answer.sort()
    return answer
