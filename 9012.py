'''
    9012 괄호
    알고리즘:
    1. 스택이 비어있으면, 괄호를 넣는데 ')'이면 끝내도 된다
    2. 비어있지 않으면, top이랑 비교해서 같은 모양이면 넣고 다르면 짝을 지어서 빼는걸 반복
    3. 짝이 다 맞았다면, stack의 len이 0일거니까 YES, 짝이 다 맞지 않으면, stack의 len이 0이 아니고 남아있을 테니까 NO
'''

def empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def top(stack):
    return stack[len(stack)-1]

T = int(input())
for i in range(T):
    s = input()
    stack = []

    for j in s:
        if empty(stack):
            if j == '(':
                stack.append(j)
            else:
                stack.append(j)
                break
        else:
            if j == top(stack):
                stack.append(j)
            else:
                stack.pop()

    if len(stack)==0:
        print("YES")
    else:
        print("NO")