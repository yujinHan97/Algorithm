'''
    알고리즘
    1. 1월 1일 부터 현재 날짜까지 days를 이용해 날 수(count)를 세어준다
    2. 첫날이 금요일이니까, count는 5부터 시작(금요일은 index 5)
    3. 총 count를 7일로 나누고, 해당 인덱스의 요일을 반환
'''
def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yo = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    count = 5 # 금요일이 시작이니까 
    for i in range(1, a): 
        count += days[i-1]
    count += (b - 1)
    
    answer = yo[count % 7]
    return answer
