'''
    알고리즘:
    1. 공백은 밀어도 공백이니까 개별적으로 경우를 나눈다
    2. 대문자인 경우, 아스키 코드 번호를 확인하고, Z를 넘어가면 A를 기준으로 다시 계산한다
    3. 소문자인 경우도, z를 넘어가면 a를 기준으로 다시 계산한다
'''
def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        
        # 대문자인 경우(A = 65, Z = 90)
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            num = ord(s[i]) + n
            if num > 90: # Z를 넘어간다면 A를 기준으로 조정
                num = 65 + (num-90) - 1
           
        # 소문자인 경우(a = 97, z = 122)
        else:
            num = ord(s[i]) + n
            if num > 122: # z를 넘어간다면 a를 기준으로 조정
                num = 97 + (num-122) -1
               
        answer += chr(num)

    return answer
