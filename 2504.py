'''
    알고리즘:
    (다시 풀기)
    1. 그려가면서 품 
    2. temp의 값을 0인지 아닌지 판별하는 부분 구글링 참고함
    3. 숫자가 나오면 값을 계속 더해서 괄호가 나오면 그 수를 2*, 3* 해서 계산
'''
import sys
input = sys.stdin.readline

bracket = input().strip()
stack = []
for x in bracket:
    if x == '(' or x == '[':
        stack.append(x)
    elif x == ')':
        temp = 0
        if len(stack) == 0:
            print(0)
            exit()
        while len(stack) != 0:
            popped = stack.pop()
            if popped == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif popped == '[':
                print(0)
                exit()
            else:
                temp += int(popped)
    elif x == ']':
        temp = 0
        if len(stack) == 0:
            print(0)
            exit()
        while len(stack) != 0:
            popped = stack.pop()
            if popped == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif popped == '(':
                print(0)
                exit()
            else:
                temp += int(popped)  
    else:
        print(0)
        exit()

answer = 0
for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit()
    else:
        answer += i
        
print(answer)
