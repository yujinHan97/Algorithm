'''
    알고리즘:
    1. 각 사람의 반복적인 패턴을 찾아서 index를 계산하고 그 index로 맞는지 확인
    2. 가장 많이 맞춘 사람의 개수를 저장하고, 그 개수와 같은 사람들을 추려낸다
'''
def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct = []
    c1 = c2 = c3 = 0
    for i in range(len(answers)):
        index = i % len(p1)
        if answers[i] == p1[index]:
            c1 += 1
    correct.append(c1)
    for i in range(len(answers)):
        index = i % len(p2)
        if answers[i] == p2[index]:
            c2 += 1
    correct.append(c2)
    for i in range(len(answers)):
        index = i % len(p3)
        if answers[i] == p3[index]:
            c3 += 1
    correct.append(c3)

    max_cor = max(correct)
    temp = []
    for i in range(1,4):
        temp.append([i, correct[i-1]])

    for i in temp:
        if i[1] == max_cor:
            answer.append(i[0])

    return answer
