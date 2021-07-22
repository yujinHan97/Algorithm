# 다른 사람 풀이
def solution(priorities, location):
    answer = 0
    # enumerate 사용법 알기!
    dq = [(i, p) for i, p in enumerate(priorities)]
    
    while True:
        cur = dq.pop(0)

        # any 사용법 알기! 
        if any(cur[1] < q[1] for q in dq):
            dq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# 내 풀이
from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque()

    for i in range(len(priorities)):
        dq.append((i, priorities[i]))

    while True:
        index, pri = dq.popleft()

        for temp_index, temp_pri in dq:
            canpop = True
            if pri < temp_pri:
                #answer += 1
                dq.append((index, pri))
                canpop = False
                index, pri = -1, -1
                break


        if canpop:
            answer += 1

        if location == index:
            return answer

    return answer
