''' 
    7568 덩치
    알고리즘 :
    1. 각 사람의 키와 몸무게를 list로 입력받아서, dungchi_list를 생성
    2. 자기 자신보다 키와 몸무게가 모두 큰 경우에만, count 수 증가
    3. count수 보다 1 큰게 자기 자신의 등수 
'''
N = int(input())

dungchi_list = []
for i in range(N):
    dungchi = list(map(int, input().split()))
    dungchi_list.append(dungchi)

for i in range(N):
    count = 0
    for j in range(N):
        if i == j: continue
        if dungchi_list[i][0] < dungchi_list[j][0] and dungchi_list[i][1] < dungchi_list[j][1]:
            count += 1

    print(count+1)