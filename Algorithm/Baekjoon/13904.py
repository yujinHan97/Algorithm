'''
    13904 과제
    알고리즘:
    (생각해내지 못해서 구글링 한 문제)
    1. 과제 점수가 높은 순으로 마감일에 최대한 가깝게 넣어준다
    (https://zzang9ha.tistory.com/207 참고)
'''
import sys

N = int(input())
hw = []
days = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    days.append(d) 
    hw.append([d,w])

max_day = max(days) # 마감일의 최대 날짜까지 과제를 할 수 있으므로
hw.sort(key = lambda x:(-x[1], x[0])) # 과제의 점수를 큰 것부터 내림차순 정렬

assign = [0 for i in range((max_day+1))]

for x in hw:
    day = x[0]
    score = x[1]
    
    # 점수가 큰 과제부터 날짜에 맞춰서 한다
    # 만약 이미 날짜에 다른 과제가 부여되어있다면, 그 전날에 한다 --> 반복
    if assign[day] == 0:
        assign[day] = score
    else:
        while day > 1: # 마감일 전의 날짜들에 대해서, 마감일과 가장 가까운 날로 배정
            day -= 1
            if assign[day] == 0:
                assign[day] = score
                break

print(sum(assign))