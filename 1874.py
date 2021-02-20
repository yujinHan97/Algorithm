'''
    1874 스택수열
    알고리즘:
    1. 입력받은 seq에서 앞 요소가 더 크면 pop을 하고 더 작으면 push를 한다
    2. 입력받은 수열을 만들기 위해서, 스택에서 pop하는 수가 seq에서의 수보다 작으면 입력받은 수열을 만들 수 없다
    3. 이러한 겨우에는 op 리스트를 초기화하고 끝내 버린다
'''
import sys
n = int(input())
seq = [] # 수열을 저장할 리스트
op = [] # 출력할 연산을 저장할 리스트
stack = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))

start = 0
for i in range(len(seq)):
    if len(stack) == 0: # 스택이 비어있으면 push
        for j in range(start+1, seq[i] + 1):
            stack.append(j)
            start = stack[len(stack)-1] # 다음 push할때 시작 할 숫자를 저장하기 위한 변수
            op.append('+')
        stack.pop() # 마지막으로 push된 숫자는 수열의 숫자니까 pop
        op.append('-')
        continue
    if seq[i] < seq[i-1]: # 수열의 현재 숫자가 이전의 숫자보다 작으면 pop
        if seq[i] >= stack[len(stack)-1]: # 수열의 현재 숫자가 스택의 top보다 작으면 pop할 수 없으니까, 크거나 같으면 pop
            stack.pop()
            op.append('-')
        else: # 수열의 현재 숫자가 스택 탑보다 작으면 pop을 할 수 없으므로, op연산 싹 다 지우고 종료
            op.clear()
            break
    else: # 수열의 현재 숫자가 수열의 이전 숫자보다 크면 그 만큼 push를 해줘야한다
        for j in range(start + 1, seq[i] + 1): # 이전 push할 때 마지막으로 저장한 수보다 큰 수 부터 수열의 현재 수까지 push
            stack.append(j)
            start = stack[len(stack)-1]
            op.append('+')
        stack.pop() 
        op.append('-')

if len(op) == 0:
    print("NO")
else:
    for i in range(len(op)):
        print(op[i])