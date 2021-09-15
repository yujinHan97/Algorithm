'''
    알고리즘:
    1. 제일 최솟값을 만드려면, 젤 큰수  * 젤 작은수 하면 된다.
    2. 하나는 오름차순 정렬, 하나는 내림차순 정렬해서 곱한걸 누적한다
'''
def solution(A,B):
    answer = 0

    A.sort(reverse = True)
    B.sort()
    
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer
