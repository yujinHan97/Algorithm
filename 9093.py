'''
     알고리즘:
     1. 문자열 뒤집어서 출력 --> [::-1] 기억하기
'''
T = int(input())

for i in range(T):
    s_list = list(map(str, input().split()))

    for i in range(len(s_list)):
        if len(s_list[i]) == 1:
            print(s_list[i], end = ' ')
        else:
            print(s_list[i][::-1], end = ' ')

    print()
