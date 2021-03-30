'''
    6549 히스토그램에서 가장 큰 직사각형
    알고리즘:
    (아직도 이해 잘 안간다. 나중에 다시 할 것)
    1. 모든 직사각형의 높이들을 탐색
    2. 스택에 자기의 높이보다 큰 높이가 없으면 stack 에 push
    3. 스택의 top이 나보다 높거나 같으면, 그 높이 pop해서 최대 넓이 계산
    4. 남은 것들을 pop해서 넓이 비교
'''
import sys

def maxArea():
    max_area = 0
    stack = []

    for i in range(N):
        index = i
        
        while stack and stack[-1][0] >= h[i]:
            height, index = stack.pop() # 현재 나의 높이가 stack top의 높이보다 작거나 같은 경우 pop
            tmp_area = height * (i-index) # i-index로 가로 계산
            max_area = max(max_area, tmp_area)

        # 맨 처음 막대인 경우 or
        # stack top의 높이보다 현재 나의 높이가 더 높은 경우 push
        stack.append([h[i], index]) 

    # 직사각형을 모두 탐색했으면, stack에 남은 것들은 pop해서 넓이 비교
    for height, index in stack:
        max_area = max(max_area, height*(N-index))

    return max_area

while True:
    h = list(map(int, sys.stdin.readline().split()))

    if h[0] == 0:
        break

    N = h[0]
    h = h[1:]
    print(maxArea())
