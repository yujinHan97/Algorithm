'''
    알고리즘:
    1. 총 재생시간과 각 장르의 재생시간을 기준으로 정렬을 해야하므로, 그냥 사전 자료형 2개를 선언
    2. dict1은 재생 시간과 인덱스, dict2은 장르별 재생 시간의 총 합으로 구성
    3. dict2의 장르별 정렬된 것마다, 2개씩 걸러내기 위해서 [:2] 사용 
'''
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dict1 = defaultdict(list)
    dict2 = defaultdict(int)
    for idx, play in enumerate(plays):
        dict1[genres[idx]].append((play, idx))
        dict2[genres[idx]] += play
     
    #### 여기 부분 
    for k, v in sorted(dict2.items(), key = lambda x:x[1], reverse = True):
        count = 0
        for p, i in sorted(dict1[k], key = lambda x:x[0], reverse = True)[:2]:
            answer.append(i)
            
    return answer
