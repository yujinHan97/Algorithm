'''
    알고리즘:
    1. 최대한 많은 부서를 지원해줘야 하므로, 신청 금액이 적은 부서들부터 지원한다
    2. 부서별 신청 금액 d배열을 오름차순 정렬 후, budget 이하인 총 금액에 대해서 부서의 수를 센다
'''
def solution(d, budget):
    answer = 0
    d.sort()
    
    total = 0
    for i in range(len(d)):
        total += d[i]
        
        if total > budget: # 예산을 넘어가면 더 이상 지원할 수 없다
            break
            
        answer += 1 # if문 다음에 배치해야 초과할 때의 경우를 세지 않는다
        
    return answer
