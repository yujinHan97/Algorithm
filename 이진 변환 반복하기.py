'''
    알고리즘:
    1. 매번 0의 개수만큼 빼서 1을 붙이고
    2. 길이를 bin() 함수 쓰고 [2:]로 잘르는 것 반복
'''
def solution(s):
    answer = []

    bin_count, total_zero = 0, 0
    while s != '1':
        zero_count = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                zero_count += 1
        
        s = (len(s) - zero_count) * '1'
        length = len(s)
        
        s = bin(length)[2:]
        bin_count += 1
        total_zero += zero_count
                
    answer.append(bin_count)
    answer.append(total_zero)
                
    return answer
