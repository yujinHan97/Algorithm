'''
    1436 영화감독 숌
    알고리즘 :
    1. i를 666부터 차례대로 검사하는데, 666이 들어가 있으면 종말 영화
    2. 666이 들어있는지 확인하기 위해서, str() 이용해서 문자열로 만들기
'''
N = int(input())

i = 666
index = 0
movies = []

while True:
    if index == N:
        break
    if '666' in str(i):
        movies.append(i)
        index += 1
    i += 1

print(movies[N-1])