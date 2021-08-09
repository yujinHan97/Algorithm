'''
    5639 이진 검색 트리
    알고리즘:
    (어려워서 구글링 한 문제)
    1. 이진 탐색 트리이므로, root를 기준으로 왼쪽과 오른쪽 서브트리를 구분한다
    2. 그런 다음에 루트를 마지막으로 출력한다
'''
import sys 
sys.setrecursionlimit(10 ** 6)

def topost(start, end):
    if start > end:
        return
    
    root = pre[start]
    div = end + 1
    for i in range(start + 1, end + 1):
        # root보다 크다면, 오른쪽 트리인 것 ==> 그 부분 기준으로 서브 트리 구분
        if root < pre[i]:
            div = i
            break

    topost(start+1, div-1) # 왼쪽 서브 트리
    topost(div, end) # 오른쪽 서브 트리
    print(pre[start]) # 후위순회는 root를 마지막으로 출력

pre = []
count = 0
while True: # 계속 입력
    try:
        pre.append(int(input()))
    except: # 예외시 중단
        break

topost(0, len(pre)-1)
