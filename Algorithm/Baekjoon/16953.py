'''
    16953 A --> B
    알고리즘:
    1. 2를 곱하면 항상 짝수만 나올것이고, 1을 붙이면 항상 홀수가 나올것이다.
    2. 따라서, B가 짝수면 2로 나누면 되고, 1로 끝나면면 1을 떼면 되고(= 10으로 나누는 것과 같다), 그 외의 경우는 break
    3. 그렇게 하다가 A와 같아진다면 횟수를 출력하면 되고, A보다 작아지면 만들 수 없는 경우이니까 -1 출력
'''
A, B = map(int, input().split())

count = 0
while True:
    if B == A:
        break
    if B < A:
        count = 0
        break
    if B % 2 == 0: 
        B /= 2
    elif B % 10 == 1:
        B = B // 10 
    else:
        count = 0
        break
    count += 1

if count == 0:
    print(-1)
else:
    print(count+1)