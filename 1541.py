'''
    1541 잃어버린 괄호
    알고리즘:
    1. 입력을 '-'를 기준으로 list에 넣어준다. 
    2. 각 리스트를 숫자로 바꾼다. 이때 +가 있으면, 숫자로 바꾸고 더한 결과값으로 저장
    3. 최소로 만들기 위해서는 최종 list에 남은 숫자들끼리 빼면된다. 
'''
s = input().split('-')
num_list =[]

for x in s:
    total = 0

    if '+' in x:
        temp = x.split('+') 
        for num in temp:
            total += int(num)
        num_list.append(total)
    else:
        num_list.append(int(x))

sumvalue = num_list[0]
for i in range(1, len(num_list)):
    sumvalue -= num_list[i]

print(sumvalue)