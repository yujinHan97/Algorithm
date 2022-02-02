'''
    알고리즘:
    (어려워서 해설, 코드 참고한 문제)
    1. 원형을 2배로 늘려서 일자 형태로 변경하여 문제 해결
    2. 모든 순열에 대해서, 해당 친구가 작업을 했을 때 그 친구가 갈 수 있는 마지막 거리보다 작업 위치가 크다면, 사람을 추가
'''
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 취약 부분 각각의 값에 n을 더해서 원형을 2배로 늘려 일자 형태로 변경
    for i in range(length):
        weak.append(weak[i] + n)    
    answer = len(dist) + 1 # 투입인원의 최솟값을 찾기 위해서, 최댓값으로 초기화 
    
    # 취약 부분 각각에 대해서 시작점으로 설정
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            last_pos = weak[start] + friends[count-1]
            for index in range(start, start+length):
                if last_pos < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    last_pos = weak[index] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        answer = -1
        
    return answer
