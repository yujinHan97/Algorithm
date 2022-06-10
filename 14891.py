'''
    알고리즘:
    1. 돌리는 톱니바퀴를 기준으로 왼쪽에 있는 톱니바퀴들과 오른쪽에 있는 톱니바퀴를 나눈다
    2. 왼쪽 톱니바퀴들 돌리고, 오른쪽 톱니바퀴들을 돌리는 과정 반복
'''
def rotate(num): #시계방향 회전
    global circle
    circle[num].insert(0, circle[num][len(circle[num])-1])
    del circle[num][len(circle[num])-1]

def antirotate(num): #반시계방향 회전
    global circle
    circle[num].append(circle[num][0])
    del circle[num][0]

# circle번호와 인덱스를 통일시키기 위해 dummy data [0]인덱스에 넣는다
circle = [[0]]
for i in range(4):
    circle.append(list(map(int, input())))

K = int(input())
method = []
for i in range(K):
    method.append(list(map(int, input().split())))

for x in method:
    tf = [False] * 5 # 각 횟수마다 돌아야 하는 톱니바퀴들을 구분할 변수 True일 때만 돈다
    num = x[0]
    rot = x[1]
    tf[num] = True # 현재 돌릴 톱니바퀴는 True로 
    
    # 현재 돌릴 톱니바퀴를 기준으로 왼쪽에 있는 바퀴들에 대해서, 서로 다른 극이라면 돌려야 하니까 True로
    for a in range(num-1, 0, -1):
        if circle[a][2] != circle[a+1][6]:
            tf[a] = True
    # 현재 돌릴 톱니바퀴를 기준으로 오른쪽에 있는 바퀴들에 대해서, 서로 다른 극이라면 돌려야 하니까 True로
    for a in range(num+1, 5):
        if circle[a][6] != circle[a-1][2]:
            tf[a] = True
            
    # 현재 횟수에서 돌릴 톱니바퀴를 회전시킴
    if rot == 1: # 시계 방향으로 회전
        rotate(num)
    else: # 반시계 방향으로 회전
        antirotate(num)

    # 방금 돌린 톱니바퀴를 기준으로 왼쪽에 있는 톱니바퀴들 중에서 True인 바퀴는 돌리는데 
    for a in range(num-1, 0, -1):
        if tf[a] == True:
            if rot == 1: # 방금 시계방향으로 돌렸다면,
                antirotate(a) # 이제 돌려야 할 바퀴는 반시계 방향으로 돌리고
                rot = -1 # 이제 반시계 방향으로 돌렸다고 저장
            else: # 반대로, 반시계방향으로 돌렸다면
                rotate(a) # 이제 돌려야 할 바퀴는 시계 방향으로 돌리고
                rot = 1 # 이제 시계 방향으로 돌렸다고 저장
        else: # False이후의 바퀴들은 안도니까 여기서 종료
            break

    # 기준 톱니바퀴의 오른쪽에 있는 바퀴들을 돌리기 위해서, 다시 기준톱니바퀴가 돌아간 방향을 설정
    rot = x[1]
    for a in range(num+1, 5):
        if tf[a] == True:
            if rot == 1:
                antirotate(a)
                rot = -1
            else:
                rotate(a)
                rot = 1
        else:
            break

# [0]에 있는 극에 따라 점수 변환
total = 0
for i in range(1, 5):
    if circle[i][0] == 1:
        total += (2 ** (i-1))
    
print(total)
