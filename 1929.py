'''
    알고리즘:
    1. 구간 내의 소수를 구하기? -> 에라토스테네스의 체 알고리즘 사용
    2. 1~n까지 모두 True로 초기화한 배열을 선언하고, 1은 False로 설정한다 (여기서 1을 False로 안했어서 틀렸었다)
    3. 2부터 n의 제곱근까지 검사하면서, 해당 수는 제외하고 그의 배수는 소수가 아님으로 설정
'''
m, n = map(int, input().split())
sosu = [True] * (n+1)
sosu[1] = False # 이것 때문에 틀렸었다. (항상 1은 False로 해놓기!)

for i in range(2, int(n**0.5)+1):
  if sosu[i] == True:
    j = 2
    while i * j <= n:
      sosu[i*j] = False
      j += 1

for i in range(m, n+1):
  if sosu[i]:
    print(i)
