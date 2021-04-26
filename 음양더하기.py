'''
    알고리즘:
    1. signs가 True이면 양수니까, 그냥 더한다
    2. signs가 False이면 음수니까, -를 붙여서 더한다
'''
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += (-absolutes[i])

    return answer
