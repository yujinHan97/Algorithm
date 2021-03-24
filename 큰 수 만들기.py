'''
    알고리즘:
    1. number에 있는 수를 하나씩 가져오면서, stack에 넣기
    2. 이 때, stack의 top < 들어가려는 수 : stack에서 pop하기
       (k를 줄여가면서)
    3. 그 외, stack의 top >= 들어가려는 수 : stack에 넣기
    4. 아직 k만큼 수를 없애지 않았다면(k>0), 뒤에서 k만큼 지우기
'''
def solution(number, k):
    answer = ''
    stack = []

    for i in number:
        # 스택이 비어있지 않으면서, 스택의 마지막 원소보다 지금 들어가려는 숫자가 큰 경우, 스택의 top 삭제
        while stack and stack[-1] < i:
            if k > 0:
                stack.pop()
                k -= 1 
            else:
                break
        # 스택이 비어잇거나, 마지막 원소가 지금 들어가려는 숫자보다 큰 경우, 그냥 삽입
        stack.append(i)

    # 위의 과정을 완료하고도 k가 0보다 크면 (= 지워야 할 수가 남았다면)
    if k>0:
        for i in range(k):
            stack.pop()

    answer = ''.join(stack)
    return answer
