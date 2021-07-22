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
