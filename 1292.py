'''
    1292 쉽게 푸는 문제
    알고리즘:
    1. list의 개수가 B가 될때 까지 숫자를 그 개수만큼 넣으면 끝
'''
A, B = map(int, input().split())

num_list = []
start, repeat = 1, 1

while len(num_list) <= B: 
    for i in range(repeat):
        num_list.append(start)

    start += 1
    repeat += 1

print(sum(num_list[A-1:B]))
