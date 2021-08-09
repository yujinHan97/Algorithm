'''
    알고리즘:
    1. 체육복을 잃어버린 학생에 대해서 여분이 있으면 자기가 먼저 입는다
    2. 만약 앞, 뒤에 여분이 있으면 빌리면 되는데, 이 때 앞 뒤의 친구가 체육복을 잃어버리지 않았어야 한다
    틀렸던 부분: 앞 뒤의 친구가 체육복을 잃어버리지 않았어야 한다는 조건을 빼먹었다
'''
def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+1)

    for i in lost: # 잃어버린 학생에 대해 체육복 0으로 설정
        students[i] = 0
    
    for i in range(1, n+1):
        if students[i] == 0: 
            if i in reserve: # 체육복을 잃어버렸는데, 내가 여분이 있는 경우
                students[i] = 1
                reserve.remove(i)
            else:
                if i-1 in reserve and students[i-1] == 1: # 앞, 뒤 친구가 체육복을 잃어버리지 않았어야 함
                    students[i] = 1
                    reserve.remove(i-1)
                elif i+1 in reserve and students[i+1] == 1:
                    students[i] = 1
                    reserve.remove(i+1)

    for i in range(1, n+1):
        if students[i] == 1:
            answer += 1

    return answer
