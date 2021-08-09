'''
    알고리즘:
    1. participant에서 이름을 key로 하는 사전을 생성
    2. 사전에서 completion 이름에 해당하는 값은 -1 
    3. completion을 다 돌고 나면 participant에서 0보다 큰 사람은 완주하지 못한 사람
'''
def solution(participant, completion):
    answer = ''
    
    part = {}
    for i in participant:
        if i in part.keys():
            part[i] += 1
        else:
            part[i] = 1

    for i in completion:
        if i in part.keys():
            part[i] -= 1
    
    for i in part.keys():
        if part[i] > 0:
            answer += i

    return answer
