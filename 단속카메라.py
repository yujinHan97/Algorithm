'''
    알고리즘:
    1. 진입/진출에 따라 일단 정렬
    2. 진출에 가장 가까울 수록 더 많은 차량을 한번에 담을 수 있으니까 첫번째 기준 카메라는 진출 지점에 설치
    3. 카메라 1대를 설치했다면, --(3-1)--진입--(3-2)--진출--(3-3)-- 이렇게 되는데 3가지의 경우의 수 나옴
       3-1) 이전에 설치한 카메라가 진입 구간보다 전에 있는 경우 => 현재 진출 구간에 카메라 추가 설치
       3-2) 이전에 설치한 카메라가 진입과 진출 구간 사이에 있는 경우 => 추가 카메라 필요 X
       3-3) 이전에 설치한 카메라가 현재 진출 구간보다 나중에 있는 경우 => 이전에 설치한 카메라를 현재 진출 구간으로 옮겨서 설치
'''
def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[0], x[1]))

    cam = routes[0][1]
    answer += 1
    for i in range(1, len(routes)):
        from_, to_ = routes[i][0], routes[i][1]
        
        # 3-1
        if cam < from_: 
            answer += 1
            cam = to_
        # 3-2
        elif from_ <= cam & cam <= to_:
            continue
        # 3-3
        elif cam > to_:
            cam = to_
            
    return answer
