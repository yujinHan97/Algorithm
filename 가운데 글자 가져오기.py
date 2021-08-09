'''
    알고리즘:
    1. 문자열의 길이 계산해서 문제 요구사항대로 풀면 된다
'''
def solution(s):
    answer = ''
    
    index = len(s) // 2
    # 길이가 짝수이면 가운데 글자 2개 출력
    if len(s) % 2 == 0:
        answer = s[index-1:index+1]
    # 길이가 홀수이면 가운데 글자 출력
    else:
        answer = s[index]
        
    return answer
