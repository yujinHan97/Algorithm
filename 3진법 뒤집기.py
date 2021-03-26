'''
    알고리즘:
    1. n이하의 3의 제곱수를 모두 찾아내서 리스트를 만든다
    2. 리스트를 역순으로 탐색하면서, 3진법을 만든다
    3. 문제에서는 3진법을 반전시켜서 다시 10진법으로 만들라고 했는데,
       굳이 반전시킬 필요 없이 인덱스로 10진법의 수를 구하면 된다
'''
def solution(n):
    answer = 0
    arr = []

    # n이하의 3의 제곱 수 찾아내기
    i = 0
    while True:
        num = 3 ** (i)  
        if num > n:
            break
        arr.append(num)
        i += 1
        
    # 찾은 3의 제곱수로 3진법 만들기
    three = ''
    while arr:
        mok = n // arr[-1] # 마지막꺼부터 검사하고 삼진법으로 바꾼 후 pop
        n -= arr[-1] * mok
        arr.pop()
        three += str(mok)

    # 인덱스로 10진법 구하기
    for i in range(len(three)):
        answer += (int(three[i]) * (3 ** (i)))

    return answer
