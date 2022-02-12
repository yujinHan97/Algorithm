'''
    알고리즘:
    1. 문제에 나와있는 대로 구현
'''
def solution(N, stages):
    answer = []
    total = len(stages)
    
    peop = [0] * N
    for i in range(1, N+1):
        count = stages.count(i)
        peop[i-1] = count
        
    fail = []
    for i in range(len(peop)):
        if total == 0:
            fail.append((i+1, 0))
            continue
            
        fail.append((i+1, (peop[i] / total)))
        total -= peop[i]
    
    fail.sort(key = lambda x:(-x[1], x[0]))

    for f in fail:
        answer.append(f[0])
    return answer
