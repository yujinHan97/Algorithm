'''
    알고리즘:
    1. 각 level마다 차례로 실패율을 구하기 위해서, stages를 정렬
    2. 전체 player수를 구하고, 해당 level에 있는 사람의 개수 세기
    3. 해당 level의 사람을 셌으면, 그 사람은 이제 없애기 pop
    4. 실패율을 모두 저장했으면 내림차순 정렬하고, level로 출력
'''
def solution(N, stages):
    answer = []

    fail = [] # 스테이지의 실패율을 저장하는 리스트
    stages.sort()
    
    for level in range(1, N+1): # level마다 실패율 검사
        count = 0
        size = len(stages)

        while True:
            # stages가 빈 배열이 아니고, level에 해당하는 stage라면,
            if stages and level == stages[0]: 
                count += 1 
                stages.pop(0) # count세고 빼기
            else: 
                break

        # 해당 level에 머물러 있는 사람 없으면, 실패율은 0
        if count == 0:
            fail.append([level, 0])
        # 해당 level의 실패율 계산
        else:
            ratio = count / size
            fail.append([level, ratio])
             
    # 실패율을 내림차순 정렬, 실패율이 같다면 level은 오름차순 정렬
    fail.sort(key = lambda x:(x[1], -x[0]), reverse = True)
    
    # 정렬된 실패율에서 level만 뽑아서 answer에 추가
    for i in fail:
        answer.append(i[0])

    return answer
