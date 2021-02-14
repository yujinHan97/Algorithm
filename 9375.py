''' 
    9375 패션왕 신해빈
    알고리즘:
    1. key = 의상의 종류, value = 해당 종류의 개수 를 바탕으로 딕셔너리를 생성
    2. 딕셔너리에서, 
        - (해당 종류의 개수 + 1)을 종류마다 곱하기 --> 입지 않은 경우도 있으므로
        - 종류마다 곱한 결과값에서 -1하기 --> 각 종류마다 입지않은 경우 즉, 알몸인 경우는 제외
'''
T = int(input())
for i in range(T):
    N = int(input())
    case = 1

    clothes = {}
    for j in range(N):
        name, kind = map(str, input().split())

        if kind in clothes.keys():
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    
    for a in clothes.items():
        case *= (a[1] + 1)

    print(case-1)