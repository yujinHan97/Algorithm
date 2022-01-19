'''
    알고리즘:
    1. 차들을 검사하면서, 시간을 측정
      - IN인데 다음 차 번호랑 같지 않으면, 11:59분에 출차한 걸로 생각
      - 위의 경우가 아닌 IN이면, 들어온 시각 저장만 
      - OUT이면, 저장된 들어온 시간과 현재 시간 차이 구해서 시간 계산
'''
import math
def solution(fees, records):
    answer = []
    car = {}
    
    s_h, s_m = 0, 0
    new_rec = []
    for i in range(len(records)):
        time, num, io = map(str, records[i].split())
        new_rec.append([time, num, io])
    # 차 번호별로 분류? 하기 위해서 번호, 시간으로 일단 정렬
    new_rec.sort(key=lambda x:(x[1], x[0]))
    
    for i in range(len(new_rec)):
        time, num, io = new_rec[i][0], new_rec[i][1], new_rec[i][2]
        h, m = map(int, time.split(":"))
        
        if num in car.keys():
            if (io == "IN" and i == len(new_rec)-1) or (io == "IN" and num != new_rec[i+1][1]):
                dur = (23-h) * 60 + 59-m
                car[num] += dur
            elif io == "OUT":
                dur = 0
                if m >= s_m:
                    dur = (h-s_h) * 60 + (m-s_m)
                else:
                    dur = (h-1-s_h) * 60 + (60+m - s_m)
                car[num] += dur    
            else:
                s_h, s_m = h, m     
        else:
            if i == len(new_rec)-1 or num != new_rec[i+1][1]:
                dur = (23-h) * 60 + (59-m)
                car[num] = dur
            else:
                s_h, s_m = h, m
                car[num] = 0 
    
    # 요금 계산 
    for key, value in car.items():
        cost = 0
        if value > fees[0]:
            value -= fees[0]
            cost += fees[1]
            plus_time = math.ceil(value/fees[2]) 
            cost += (plus_time * fees[3])
        else:
            cost = fees[1]
        answer.append(cost)
    return answer
