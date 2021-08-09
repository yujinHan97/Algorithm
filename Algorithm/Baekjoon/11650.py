'''
    11650 좌표 정렬하기
    알고리즘 :
    1. x, y를 하나의 리스트에 담고, 여러개의 x,y들을 coord라는 리스트에 담아서 sort() 함수 사용해 정렬
'''
N =int(input())
coord = []

for i in range(N):
    a = list(map(int, input().split()))
    coord.append(a)

coord.sort()
for i in range(len(coord)):
    print(coord[i][0], coord[i][1])
