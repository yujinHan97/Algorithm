'''
    알고리즘:
    1. dict 자료형 사용해서 문제 요구사항 대로 구현
'''
def solution(id_list, report, k):
    answer = []
    reported = {}
    ids = {}
    report = list(set(report))
    for i in range(len(report)):
        s, r = map(str, report[i].split())
        if r in reported.keys():
            reported[r] += 1
        else:
            reported[r] = 1
            
    for user in id_list:
        if user not in ids.keys():
            ids[user] = 0
            
    # print(ids)
    reported_list = []
    for key,value in reported.items():
        if value >= k:
            reported_list.append(key)
           
    # print(reported_list)
    # temp = []
    for i in range(len(report)):
        s, r = map(str, report[i].split()) 
        if r in reported_list:
            ids[s] += 1
    # print(ids)
    for key, value in ids.items():
        answer.append(value)
    
    return answer
