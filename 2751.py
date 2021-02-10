'''
    2751 수 정렬하기 2 
    알고리즘 : 
    1. sort() 함수 이용하기
'''
N = int(input())
array = []
sorted = []

for i in range(N):
    a = int(input())
    array.append(a)

array.sort()

for i in range(N):
    print(array[i])
