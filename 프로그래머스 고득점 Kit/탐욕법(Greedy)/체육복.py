'''
    알고리즘:
    1. 모든 학생들을 체육복이 있다고 가정하고 1로 설정
    2. 여분 학생, 잃어버린 학생 모두 check해서 +1, -1씩 한다
    3. 학생들 모두를 검사하면서 2개의 체육복이 있으면 앞, 뒤에 0인 학생에게 빌려주면서 -1, +1을 각각 연산
'''
def solution(n, lost, reserve):
    answer = 0
    
    arr = [1] * (n+1)
    for num in lost:
        arr[num] -= 1
    for num in reserve:
        arr[num] += 1
    
    for i in range(1, n+1):
        if arr[i] == 2:
            if arr[i-1] == 0:
                arr[i] -=1
                arr[i-1] += 1
            elif i != n and arr[i+1] == 0:
                arr[i] -= 1
                arr[i+1] += 1
                
    for i in range(1, n+1):
        if arr[i] >= 1:
            answer += 1
            
    return answer
