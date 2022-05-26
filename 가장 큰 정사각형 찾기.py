'''
    알고리즘:
    (처음에 완탐으로 풀었다가 효율성 0점 => 완탐은 최소 3중 포문, dp는 2중 포문)
    (dp 생각해내지 못해서 구글링해서 풀었음)
    1. 현재 위치가 1일 때, 윗대각선, 위, 왼쪽 모두 1이면 정사각형 가능
    2. 이런 방식으로 쌓아 나가기 
'''
def solution(board):
    answer = 0

    w, h = len(board[0]), len(board)
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0:
                continue
            else:
                if board[i][j] == 1:
                    if board[i-1][j-1] != 0 and board[i-1][j] != 0 and board[i][j-1] != 0:
                        board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                    
    max_len = max(map(max, board))
    answer = max_len**2
    
    return answer
