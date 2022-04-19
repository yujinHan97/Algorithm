N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    members.append([int(age), name, i]) # members에 들어온 순서를 i로 저장하기

members.sort(key = lambda x:(x[0], x[2])) # 나이로 먼저 정렬을 하고, 나이가 같으면 들어온 순서인 x[2]로 정렬

for member in members:
    print(member[0], member[1])
