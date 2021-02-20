'''
    1874 스택수열
    알고리즘:
    1. 입력받은 seq에서 앞 요소가 더 크면 pop을 하고 더 작으면 push를 한다
    2. 입력받은 수열을 만들기 위해서, 스택에서 pop하는 수가 seq에서의 수보다 작으면 입력받은 수열을 만들 수 없다
    3. 이러한 겨우에는 op 리스트를 초기화하고 끝내 버린다
'''
import sys
n = int(input())
seq = []
op = []
stack = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))

start = 0
for i in range(len(seq)):
    if len(stack) == 0:
        for j in range(start+1, seq[i] + 1):
            stack.append(j)
            start = stack[len(stack)-1]
            op.append('+')
        stack.pop()
        op.append('-')
        continue
    if seq[i] < seq[i-1]:
        if seq[i] >= stack[len(stack)-1]:
            stack.pop()
            op.append('-')
        else:
            op.clear()
            break
    else:
        for j in range(start + 1, seq[i] + 1):
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