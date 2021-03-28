'''
    알고리즘:
    1. arr배열에서 하나씩 검사하면서 연속하지 않으면 answer배열에 넣기
    2. arr배열의 뒤에서 부터 진행 (pop(0)은 O(N)이지만, pop()은 O(1)이라서)
    3. pop한 수가 answer배열의 제일 마지막이랑 같으면 연속된거니까 무시
    4. pop한 수가 answer배열의 제일 마지막이랑 다르면 연속되지 않은거니까 append
    5. 뒤에서부터 진행했으니까 reverse한다
'''
def solution(arr):
    answer = []

    answer.append(arr.pop())
    for i in range(len(arr)-1, -1, -1):
        a = arr.pop()
        
        if a != answer[-1]:
            answer.append(a)

    answer.reverse()

    return answer
