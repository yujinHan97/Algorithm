'''
    알고리즘:
    1. 사전순으로 출력할 것이기 때문에 alpha를 입력받자마자 정렬
    2. 조합을 이용해서, 모음 자음 개수에 따라 만족하면 join해서 출력
'''
import itertools

l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()

for p in list(itertools.combinations(alpha, l)):  
  password = ''.join(p)
  mo = password.count('a') + password.count('e') + password.count('i') + password.count('o') + password.count('u')
  ja = l - mo

  if mo >= 1 and ja >= 2:
    print(password)
