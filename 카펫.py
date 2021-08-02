'''
    알고리즘:
    1. yellow의 약수 쌍을 다 구해서 각각 *2 + 4(각 꼭짓점) 한 값이 brown 과 같은 경우를 찾기
    2. 찾았으면, 각 수에 +2 씩 한게 결국 가로, 세로이다
'''
def solution(brown, yellow):
    answer = []

    # yellow의 약수 쌍을 담을 list
    pair = [(1, yellow)] 
    # 약수 찾기
    for i in range(2, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            pair.append((i, yellow//i))

    for a, b in pair:
        if 2 * (a + b) + 4 == brown:
            answer.append(b+2)
            answer.append(a+2)
            break

    return answer
