'''
    1. 중복을 없애야 하니까 dict 자료형을 사용
    (set 함수를 쓰려다가 못 썼다)

    +) sorted(list(set(array))) 로 set을 list로 변환하고 그 다음에 정렬하면 된다
'''
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))
dict = {}

for i in array:
    if i not in dict.keys():
        dict[i] = 1
array = sorted(dict.items(), key = lambda x :x[0])

for i in array:
    print(i[0], end = ' ')
