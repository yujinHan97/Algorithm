'''
    알고리즘:
    1. dp 이용
    2. 이 전 단계에서 col 인덱스가 같지 않은 것들 중에서 가장 큰 것을 쌓아나가서 제일 큰 값 찾기
'''
def solution(land):
    dp_land = [[0, 0, 0, 0]]
    for i in range(len(land)):
        dp_land.append(land[i])

    for i in range(1, len(dp_land)):
        for j in range(4):
            temp = []
            for k in range(4):
                if j == k:
                    continue
                temp.append(dp_land[i-1][k]) 
            dp_land[i][j] = dp_land[i][j] + max(temp)
            
    return max(map(max, dp_land))
        
