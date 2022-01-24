'''
    알고리즘:
    1. isdigit() 함수를 이용해서 숫자인지 아닌지 판별하여 서로 다른 리스트로 분류
    2. 문자들은 정렬 후, join()으로 문자열 합치기
'''
S = input()

char = []
num = []
for lett in S:
  if lett.isdigit():
    num.append(int(lett))
  else:
    char.append(lett)

total = sum(num)
char.sort()
new_str = ''.join(char)
new_str += str(total)
print(new_str)
