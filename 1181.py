'''
    1181 단어 정렬
    알고리즘 :
    - 통계학에서 최빈값 구하듯이, 
    1. 중복을 없애기 위해서, 딕셔너리에 (단어, 길이) 형태로 입력
    2. 딕셔너리를 lambda함수를 이용하여 길이로 먼저 정렬하고, 알파벳순으로 정렬
'''
N =int(input())
dict = {}
words = []

for i in range(N):
    words.append(input())
    length = len(words[i])
    dict[words[i]] = length

a = sorted(dict.items(), key=lambda x : (x[1], x[0]))

for i in a:
    print(i[0])


