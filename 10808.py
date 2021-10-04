'''
    알고리즘 :
    1. ord() 사용 ==> 유니코드에 대한 정수 반환하는 함수
'''
s = input()

alpha = [0] * 26
for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    alpha[index] += 1
    
for i in range(26):
    print(alpha[i], end = ' ')
