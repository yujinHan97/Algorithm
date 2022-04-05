'''
    알고리즘:
    1. 중복된 사이트는 없으니까, 사전 자료형 사용
    2. url에 해당하는 pwd 출력하면 된다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwd_dict = {}
for _ in range(n):
  addr, pwd = map(str, input().split())
  pwd_dict[addr] = pwd
  
for _ in range(m):
  url = input().strip()
  print(pwd_dict[url])
