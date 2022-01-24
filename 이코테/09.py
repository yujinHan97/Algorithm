'''
    알고리즘:
    1. 1부터 문자열의 길이의 1/2 만큼 축약할 수 있으므로, 모든 경우의 수에서 압축
    2. 주의할 점은 원래 s의 길이가 1인 경우이다 (여기서 틀려서 질문 참고함)
    3. first, second가 같으면 count를 증가시켜서 중복된다는 것 
    4. first, second가 다르면
        4-1 : count가 1이 아니면, first가 중복된 횟수니까 first를 수만큼 붙이기
        4-2 : count가 1이면, first가 중복된것도 아니고 1번 나온거니까 그냥 붙이기
'''
def solution(s):
    comp = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2 + 1):
        count = 1
        new_str = ""
        for j in range(0, len(s), i): # i씩 증가!
            first = s[j:j+i]
            second = s[j+i:j+2*i]
            if first == second: 
                count += 1
            else: # 중복되지 않는 경우, count가 1이 아니면 반복된 거니까 first를 count만큼 이어붙이기
                if count != 1:
                    new_str += (str(count) + first) 
                else: # count가 1인 경우에는 반복되지 않았으니까 그냥 이어붙이기
                    new_str += first
                count = 1
                
        comp.append((new_str, len(new_str)))
    comp.sort(key=lambda x:(x[1])) 

    return comp[0][1]
