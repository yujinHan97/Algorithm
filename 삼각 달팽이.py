'''
    알고리즘:
    (풀긴 풀었으나, 다른 사람 답을 보니 너무 어지럽고 이상한 코드인 것 같다)
    1. 다른 사람 풀이 : 3개의 방향이 반복되니까 %3의 값으로 방향 결정
    2. 아래, 오른쪽, 위쪽 => 각각 좌표를 조작
'''
def solution(n):
    tri = [[0 for _ in range(n)] for _ in range(n)]
    answer = []
    
    x, y, num = -1, 0, 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
                
            tri[x][y] = num
            num += 1
    
    for i in range(n):
        for j in range(n):
            if tri[i][j] != 0:
                answer.append(tri[i][j])
    return answer 

# 내풀이 -------------------------------------------------------------------------------
def solution(n):
    answer = []
    tri = [[0 for _ in range(n)] for _ in range(n)]
    rev_num, num = n, 1
    
    dr, dc = 0, 0
    rr, rc = n-1, 1
    lr, index = n-2, 0
    while True:
        if rev_num == 0:
            break
        
        for i in range(dr, dr + rev_num):
            tri[i][dc] = num
            num += 1
        rev_num -= 1
        dr += 2
        dc += 1
        
        if rev_num == 0:
            break
            
        for i in range(rc, rc + rev_num):
            tri[rr][i] = num
            num += 1
        rev_num -= 1
        rr -= 1
        rc += 1
        
        if rev_num == 0:
            break
            
        for i in range(lr, lr - rev_num, -1):
            tri[i][i-index] = num
            num += 1
        rev_num -= 1
        lr -= 1
        index += 1
        
        if rev_num == 0:
            break
        
    for i in range(len(tri)):
        for j in range(len(tri[0])):
            if tri[i][j] != 0:
                answer.append(tri[i][j])
                
    return answer
