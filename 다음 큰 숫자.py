'''
    알고리즘:
    1. bin() 함수 이용해서 이진수로 만들고, 0b가 붙으므로 [2:]로 자른다
    2. 입력된 자연수보다 큰 수 중에서, bin으로 변환한 값의 1의 개수가 같으면 반환
    3. 다르면, 1 증가해서 반복
'''
def solution(n):    
    temp = n + 1
    n = bin(n)
    binary_n = n[2:]
    
    while True:
        bin_temp = bin(temp)
        bin_temp = bin_temp[2:]
        
        if bin_temp.count('1') == n.count('1'):
            return temp
        
        else:
            temp += 1
