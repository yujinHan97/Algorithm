'''
    알고리즘:
    (알고리즘은 생각했으나, 구현을 못한 문제)
    1. 문자열을 1부터 N/2 까지 잘라서 압축한 경우 중에 최소 길이를 뽑는다
'''
def solution(s):
    answer = len(s)
    # 자르는 단위의 개수를 step으로 표현
    for step in range(1, len(s)//2 + 1): 
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            # 이전 글자와 동일한 글자라면, count + 1
            if prev == s[j:j+step]:
                count += 1
            # 이전 글자와 다른 글자라면, 압축 후 초기화
            else:
                if count >= 2: # 중복횟수가 2 이상이면, 숫자를 붙여서 압축
                    compressed += str(count) + prev
                else: # 중복횟수가 1이면, 그냥 글자 붙여서 압축
                    compressed += prev

                # 다시 상태 초기화
                count = 1
                prev = s[j:j+step]

        # 남은 문자열에 대한 처리
        if count >= 2: 
            compressed += str(count) + prev
        else: 
            compressed += prev

        answer = min(answer, len(compressed))

    return answer
