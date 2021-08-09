'''
    1475 방번호
    알고리즘:
    1. 입력을 한글자씩 int로 바꿔서 해당 인덱스에 횟수를 추가한다
    2. 6과 9는 혼용이 가능하니까 두 숫자의 출현 횟수를 더해서 올리면 최소로 필요한 세트 갯수
    3. 숫자들의 출현 횟수중에서 가장 큰 수가 최소로 필요한 세트 갯수이다
'''
import math

N = input()
num_list = [0] * 10

for i in range(len(N)):
    num_list[int(N[i])] += 1

a = max(num_list[6], num_list[9])
newvalue = math.ceil((num_list[6] + num_list[9]) / 2)

if a == num_list[6]:
    num_list[6] = newvalue
else:
    num_list[9] = newvalue

print(max(num_list))