'''
    5430 AC
    - 입력 받는거 까다로운 문제
    - 알고리즘 생각해내기 어려웠던 문제
    - 시간초과 받은 문제 
    ==> 다시풀기 
    알고리즘: 
    1. R인 경우에는, R의 개수를 센다
    2. D인 경우에, R의 개수를 보고 홀수면 뒤에서 제거하고 짝수면 앞에서 제거
    3. 중요! 그리고 마지막에 R의 개수가 홀수면 뒤집어 주어야 한다 !! 
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(",")
    dq = deque(arr)

    if n == 0:
        dq = []
    count = 0
    for op in p:
        flag = 0
        if op == 'R': # R일때마다 매번 뒤집으면 시간초과 --> R의 개수를 세서 짝수면 앞에서 빼고 홀수면 뒤에서 빼는 로직 사용
            count += 1

        elif op == 'D':
            if len(dq) == 0:
                msg = "error"
                flag = 1
                break
            else:
                if count % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if count % 2 == 1:
        dq.reverse()

    if flag == 1:
        print("error")
    else:
        dq = list(dq) 

        print("[", end = '')
        for i in range(len(dq)):
            print(dq[i], end = '')
            if i != len(dq) -1:
                print(',', end = '')
        print("]")
