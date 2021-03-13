'''
    알고리즘:
    1. strings배열의 인덱스와 n번째 글자를 튜플로 새로운 리스트를 생성하고,
    2. 그 리스트를 정렬
    3. 정렬된 리스트의 튜플값인 인덱스를 이용해서 strings배열에서 그 인덱스를 활용해서 answer 찾기
'''
def solution(strings, n):
    answer = []
    charAtn = []
    strings.sort() # abce, abcd (n=2)일때 'c'로 같은 경우, 사전 순 정렬을 위해서 미리 정렬 수행

    for i in range(len(strings)):
        charAtn.append((strings[i][n],i)) 
    charAtn.sort(key = lambda x:x[0]) 

    for i in range(len(charAtn)):
        answer.append(strings[charAtn[i][1]])

    return answer
