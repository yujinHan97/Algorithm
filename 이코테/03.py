'''
    알고리즘:
    (내 풀이 -> 그리디 알고리즘을 사용한 건 아님)
    1. 변하는 횟수를 구해서 /2를 하고 올림을 하면 최소 횟수이다
    
    (책 풀이 -> 그리디 알고리즘 사용)
    1. 문자열에서 모두 0으로 바꾸는 횟수 세기 (1인 경우를 세면 된다)
    2. 문자열에서 모두 1으로 바꾸는 횟수 세기 (0인 경우를 세면 된다)
    3. 둘 중, min 값을 출력
'''

# 내풀이
import math
S = input()

count = 0
for i in range(1, len(S)):
  if S[i] != S[i-1]:
    count += 1

print(math.ceil(count/2))

# 책풀이
S = input()

zeroToOne, oneToZero = 0, 0
if S[0] == '1':
  oneToZero = 1
else:
  zeroToOne = 1

for i in range(len(S)-1):
  if S[i] != S[i+1]:
    if S[i+1] == '1':
      oneToZero += 1
    else:
      zeroToOne += 1

print(min(zeroToOne, oneToZero))
