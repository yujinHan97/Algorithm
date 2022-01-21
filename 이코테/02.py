'''
    알고리즘:
    1. +, *를 해서 가장 큰 수가 되기 위해서는 보통 *를 해야 커진다.
    2. 0, 1의 숫자인 경우는 예외이다. 
    3. 따라서, 원래의 result가 0, 1이거나 현재 처리하려는 수가 0,1이면 +, 그 외의면 * 수행
'''
S = input()

result = 0
for i in range(len(S)):
  num = int(S[i])

  if i == 0: # 첫번째 글자는 저장만 해놓고 넘기기
    result = num 
    continue

  if result == 0 or result == 1 or num == 0 or num == 1:
    result += num
  else:
    result *= num

print(result)
