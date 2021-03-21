'''
    1406 에디터
    알고리즘:
    (리스트 1개로 cursor를 조작하면서 remove, insert로 해서 시간초과가 나왔다
     따라서, stack을 2개 이용하여 O(1)로 추가와 삭제를 할 수 있도록 하였다)
    1. L(커서를 왼쪽으로): s1이 비어있지 않다면 s1의 top을 pop하여 s2에 추가
    2. D(커서를 오른쪽으로): s2가 비어있지 않다면 s2의 top을 pop하여 s1에 추가
    3. B(문자 삭제): s1이 비어있지 않다면, s1의 top을 pop
    4. P(문자 추가): s1에 추가
    5. 문자열을 출력할때는 s1을 순서대로, s2는 역순으로
'''
import sys

s1 = list(sys.stdin.readline().strip())
s2 = []
N = int(input())    
for i in range(N):
    op = sys.stdin.readline().split()
    
    if op[0] == 'L':  
        if len(s1) == 0:
            continue
        s2.append(s1.pop())
    elif op[0] == 'D':
        if len(s2) == 0:
            continue
        s1.append(s2.pop())
    elif op[0] == 'B':
        if len(s1) == 0:
            continue
        s1.pop()
    elif op[0] == 'P':
        s1.append(op[1])

print(''.join(s1 + s2[::-1]))