'''
    1158 요세푸스 문제
    알고리즘:
    1. index를 K-1만큼 높여가면서 해당 인덱스 요소를 요세푸스 수열에 넣고 삭제한다
    2. 인덱스는 남아있는 리스트의 길이보다 작아야한다
    3. 위 과정 반복
    +) 리스트 = "특정문자열".join(리스트) --> 리스트는 문자열로 되어있어야 하고, 특정 문자열로 연결된 리스트가 반환된다
'''
N, K = map(int, input().split())
array = []
for i in range(N):
    array.append(i+1)

index = K-1
josephus = []
while len(array) != 0:
    if index >= len(array):
        while index >= len(array):
            index = index - len(array)
    josephus.append(array[index])
    array.remove(array[index])
    index = index + (K-1)

for i in range(N):
    josephus[i] = str(josephus[i]) # join() 함수를 사용하기 위해서 str형태로 변환

josephus = ", ".join(josephus) 
print("<", end = '')
print(josephus, end = '')
print(">")