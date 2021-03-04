'''
    알고리즘:
    1. 각 move마다 뽑힌 인형들을 basket에 담는다
    2. basekt을 담을 때마다 바로 전에 basket에 담긴 인형과 같은지 비교
'''
def solution(board, moves):
    answer = 0
    basket = []
    top = -1

    for i in range(len(moves)):
        col = moves[i] - 1

        for j in range(len(board)):
            if board[j][col] != 0:
                basket.append(board[j][col]) # 인형을 뽑고나서 옮기고, 0으로 설정
                top += 1
                board[j][col] = 0
                break
        
        if top >= 1: # 인형이 2개 이상 있는 경우, 위의 인형과 아래 인형이 같다면 제거 하고 개수 
            if basket[top] == basket[top-1]:
                basket.pop()
                basket.pop()
                answer += 2
                top -= 2

    return answer
