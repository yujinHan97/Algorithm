'''
    알고리즘:
    1. 8진수를 2진수로 표현하기 위해서, 8 -> 10 -> 2로 변환
    2. n진수 -> 10진수 : int(n진수 표현, n)
    3. 10진수 -> 2진수 : bin()
'''
octnum = input()
oct_prefix = '0o'
new_oct = oct_prefix + octnum
normal = int(new_oct, 8) # 8진수 -> 10진수 

print(bin(normal)[2:]) # 10진수 -> 2진수('0b'빼기 위해서 [2:])
