'''
    알고리즘:
    1. 체스판의 맨왼쪽 위에 있는 글자를 기준으로 매칸을 비교한다
    2. 체스판이 다른 칸이 있을 때마다 1씩 증가
    3. 64칸 중에 32칸 이상이 다르다면, 반대로 바꾸는게 나으니까 64에서 count수를 뺀다
    4. count수를 다 저장하고, 제일 최솟값을 고른다
'''
N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(input())

b_chess = ['BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB']
w_chess = ['WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW']

ccount = []
for i in range(N-8+1):
    for j in range(M-8+1):
        count = 0
        if chess[i][j] == 'B':
            for x in range(8):
                for y in range(8):
                    if chess[i+x][j+y] != b_chess[x][y]:
                        count += 1
        else:
            for x in range(8):
                for y in range(8):
                    if chess[i+x][j+y] != w_chess[x][y]:
                        count += 1

        if count > 32:
            count = 64 - count
        ccount.append(count)

print(min(ccount))
