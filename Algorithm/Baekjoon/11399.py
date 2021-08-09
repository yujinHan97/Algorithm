'''
    11399 ATM
    알고리즘 :
    1. 각 사람마다 돈을 인출하는데에 소요하는 시간을 저장한 list를 오름차순 정렬
    2. 앞에 사람이 적게 걸릴 수록 내가 기다리는 시간이 적어지니까
    3. 내가 기다려야 하는 시간은 앞에 사람들 시간 + 나의 시간
'''
N = int(input())
person = list(map(int, input().split()))
person.sort()

waiting = []
waiting.append(person[0])
for i in range(1, N):
    waiting.append(waiting[i-1] + person[i])

w_sum = 0
for i in range(N):
    w_sum += waiting[i]

print(w_sum)