'''
    알고리즘:
    1. 횟수를 가장 적게 해야 하니까, 일단 가장 무거운 사람 먼저 태우기 ==> 역순 정렬
    2. 가장 무거운 사람을 태우고 나서, 태울 수 있는 사람들 중 가장 가벼운 사람을 더 태울 수 있다면 횟수는 증가하지 않고, people에서만 제거
    3. 가장 가벼운 사람도 태우지 못한다면 횟수를 + 1
'''
from collections import deque
def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    dq = deque(people)
    while dq:
        remain = limit - dq.popleft()
        answer += 1

        if dq and remain >= dq[-1]:
            dq.pop()

    return answer
