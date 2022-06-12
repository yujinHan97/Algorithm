'''
    알고리즘:
    1. 시간이 단축하기 위해, 이미 dict변수에 저장된 값이 있으면 불러온다
    2. 만약 dict변수에 저장된 값이 없으면 값을 넣어준다
'''
import sys
dict = {} # 계산된 w값들을 저장할 dict 변수

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1

        global dict
        if a > 20 or b > 20 or c > 20:
            if (a, b, c) not in dict.keys():
                dict[(a, b, c)] = w(20, 20, 20)

            return dict[(a, b, c)]
        if a < b and b < c:
            if (a, b, c) not in dict.keys():
                dict[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        
            return dict[(a, b, c)]
        else:
            if (a, b, c) not in dict.keys():
                dict[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
            return dict[(a, b, c)]
        
    print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c)))
