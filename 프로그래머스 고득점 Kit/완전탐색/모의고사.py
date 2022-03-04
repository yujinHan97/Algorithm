'''
    알고리즘:
    1. 수포자의 pattern을 파악해서 각각의 list를 만든다
    2. 나머지 연산으로 완전탐색 비교하여 맞은 개수를 센다
    3. 맞은 개수의 max값을 구해서 사람을 출력
'''
def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len_first = len(first)
    len_second = len(second)
    len_third = len(third)
    
    a, b, c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i % len_first]:
            a += 1
        if answers[i] == second[i % len_second]:
            b += 1
        if answers[i] == third[i % len_third]:
            c += 1
    
    score = [a, b, c]
    for idx, sc in enumerate(score):
        if sc == max(score):
            answer.append(idx+1)
            
    return answer
