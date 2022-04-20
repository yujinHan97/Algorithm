'''
    알고리즘:
    1. 거듭제곱인 B의 경우에 따라 계산 구분
    2. B가 홀수인 경우(5), A^4 * A 이고, A^4는 재귀 호출
    3. B가 짝수인 경우(4), (A^2)^2 로 계산 가능 
'''
import sys
input = sys.stdin.readline

# 행렬의 곱 계산 한 후, 1000으로 나눈 나머지를 저장하는 함수
def matrix_mul(A, B):
    result = [[0] * N for _ in range(N)]

    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000

        return A

    # 홀수인 경우, 마지막에 A를 한번 곱해줘야 함
    # A^5 = (A^2)^2 * A
    elif B % 2 == 1: 
        C = matrix_mul(A, B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += C[i][k] * A[k][j] 

        for i in range(N):
            for j in range(N):
                result[i][j] %= 1000

        return result
    # 짝수인 경우, 제곱수로 계속해서 곱함
    # A^4 = (A^2)^2
    else:
        C = matrix_mul(A, B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += C[i][k] * C[k][j] 

        for i in range(N):
            for j in range(N):
                result[i][j] %= 1000

        return result

N, B = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = matrix_mul(matrix, B)

# 행렬 출력
for i in result:
    for x in i:
        print(x, end = ' ')
    print()
