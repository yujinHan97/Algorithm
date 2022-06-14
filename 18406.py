'''
    알고리즘:
    1. 입력받은 문자열의 왼쪽 반은 left에 오른쪽 반은 right에 넣는다
    2. left 리스트의 문자들을 ord를 이용하여 숫자를 변환하고 sum을 구하고
    3. right도 마찬가지로 sum을 구한다
    4. 각 sum이 같으면 LUCKY, 아니면 READY
'''
N = str(input())
length = len(N)
left = []
right = []

for i in range(length//2):
    left.append(N[i])
for i in range(length//2, length):
    right.append(N[i])

lsum = rsum = 0
for i in left:
    lsum += ord(i)
for i in right:
    rsum += ord(i)

if (lsum== rsum):
    print("LUCKY")
else:
    print("READY")
