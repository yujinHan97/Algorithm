'''
    2108 통계학
    알고리즘 :
    1. 산술평균 : sum() 내장함수 이용
    2. 중앙값 : N // 2 번째 요소 
    3. 최빈값 : 가장 어려웠던 부분. 
                1. 딕셔너리를 선언하고, array의 요소를 key로 하고, 그 키가 있으면 count를 1증가, 없으면 1로 설정
                ----------- 여기까지는 생각했던 것 --------------
                2. lambda식을 활용해서 값을 기준으로 딕셔너리를 내림차순으로 정렬
                3. dict[0][0]과 dict[0][1]이 같지 않다면, dict[0][0]이 최빈값이므로 그대로 출력
                                             같아면, 최빈값이 여러개란 의미이므로 dict[1][0]을 출력
    4. 범위 : sort해서 마지막 원소 - 첫번째 원소
'''
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
array.sort()

#산술 평균 구하기
avg = sum(array) / N 

# 중앙값 구하기 (N은 홀수라고 가정한다고 주어짐)
med = array[N//2]

# 최빈값 구하기
dict = {}
for key in array:
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1
dict = sorted(dict.items(), key = lambda dict : dict[1], reverse = True)  # 빈도수를 기준으로 dictionary 내림차순 정렬

if N != 1: 
    if dict[0][1] == dict[1][1]: # 최빈값이 여러 개 있으면, 두번째 작은 값으로 선정
        mode = dict[1][0]
    else: 
        mode = dict[0][0]
else:
    mode = dict[0][0]

# 범위 구하기
arr_range = array[N-1] - array[0]

print(round(avg))
print(med)
print(mode)
print(arr_range)