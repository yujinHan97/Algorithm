'''
    7453 합이 0인 네 정수
    알고리즘:
    1. A, B, C, D의 배열이 최대 4000개 가능이니까 for문으로 모든 경우의 수 돌리면 100퍼 시간초과
    2. 그래서 A랑 B 더한 배열 하나 만들고 C랑 D 더한 배열 하나 만들어서 AB와 CD배열의 합이 0인걸 찾는 로직 이용 
    3. CD배열은 dict로 만들어서 해시로 찾게 해서 시간 줄이기 (dict로 할 생각 처음에 못했었다..! 힌트 보고 dict 이용했당)
'''
import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D, AB, CD = [], [], [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        AB.append(A[i]+B[j]) 
        CD.append(C[i]+D[j])

CD_dict = {} # O(1)로 가능하니까 dict 사용
count = 0
for i in range(len(CD)):
    if CD[i] in CD_dict.keys():
        CD_dict[CD[i]] += 1
    else:
        CD_dict[CD[i]] = 1

for i in range(len(AB)):
    target = -1 * AB[i] # 0을 만들어야 하기 때문에 부호 바꿔서 찾기

    if target in CD_dict.keys():
        count += CD_dict[target]

print(count)
