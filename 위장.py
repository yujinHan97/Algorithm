'''
    알고리즘:
    1. 사전 자료형을 만들어서 각 옷 종류에 대하여 몇 개가 있는지에 대해서 만들어 준다
    2. 경우의 수를 구하기 위해서 개수에다가 + 1을 한 값을 answer에 곱해준다 (+1은 그 종류를 입지 않는 것)
    3. 모든 종류마다 곱하고 나면, 모든 경우의 수가 나오는데 거기서 -1 을 한다 (-1은 모든 종류를 입지 않은 것)
'''
def solution(clothes):
    answer = 1
    
    # 사전 자료형 만들기
    c = {}
    for i in clothes:
        # 이미 있는 옷 종류라면, value를 +1 
        if i[1] in c.keys():
            c[i[1]] += 1
        # 아직 없는 옷 종류라면, 옷 종류를 넣고 1로 설정
        else:
            c[i[1]] = 1
            
    for value in c.values():
        answer *= (value + 1)
        
    return answer-1
