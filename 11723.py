'''
    알고리즘:
    1. 집합 추가 연산 -> add()
    2. 집합에서 삭제 연산 -> remove(), discard()
       remove(item) : item에 해당하는 원소를 제거하고, 없으면 Keyerror 발생
       discard(item) : item에 해당하는 원소를 제거하고, 없어도 에러를 발생하지 않음
'''
import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
  operation = input().split()

  if len(operation) == 1:
    if operation[0] == "all":
      s = set([i for i in range(1, 21)])  
    else:
      s = set()
    continue
    
  op, num = operation[0], int(operation[1])
  if op == "add":
    s.add(num)
    
  elif op == "remove":
    s.discard(num)
    
  elif op == "check":
    if num in s:
      print(1)
    else:
      print(0)
      
  elif op == "toggle":
    if num in s:
      s.discard(num)
    else:
      s.add(num)
   
