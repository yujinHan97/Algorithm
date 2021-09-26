'''
    알고리즘:
    1. W인 경우, 이긴횟수 count를 증가하고, 또 다시 if문 검사해서 자신보다 몸무게 많이 나가면 heavier를 증가
    2. 정렬할 모든 요소를 한 튜플로 넣고, lambda함수 이용해서 정렬
'''
def solution(weights, head2head):
    answer = []
    win_rate = []
    for i in range(len(head2head)):
        count, heavier = 0, 0
        total = len(head2head[i])-head2head[i].count('N')
        for j in range(len(head2head)):
            if i == j: 
                continue
            else:
                if head2head[i][j] == 'W':
                    count += 1
                    if weights[i] < weights[j]:
                        heavier += 1
    
        # 승률 구하기
        if total == 0:
            first = 0
        else:
            first = count / total * 100
        # 자신보다 무거운 상대 이긴 횟수
        second = heavier
        # 자신 몸무게
        third = weights[i]
        
        win_rate.append((i+1, first, second, third))
        win_rate.sort(key = lambda x:(x[1], x[2], x[3], -x[0]), reverse = True)

    for i in range(len(win_rate)):
        answer.append(win_rate[i][0])
    return answer
