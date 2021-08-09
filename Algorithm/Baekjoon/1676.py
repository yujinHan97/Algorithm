'''
    1676 팩토리얼
    알고리즘:
    1. 팩토리얼 결과 값을 구하고, string으로 바꿔준다
    2. 문자열 형태인 결과값을 뒤에서부터 0이면 카운트 1 증가
'''
def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * factorial(N-1)

N = int(input())
result = str(factorial(N))

count = 0
for i in range(len(result)-1, -1, -1):
    if result[i] == '0':
        count += 1
    else:
        break

print(count)