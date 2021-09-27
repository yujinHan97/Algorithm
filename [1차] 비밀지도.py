'''
    알고리즘:
    1. bin() 함수 이용 : '0b______'의 형태로 반환하여 [2:]로 잘랐다
    2. n보다 부족한 만큼 0을 앞에 붙여주었고, 모두 벽이 아닌 경우(모두 0인 경우)에만 공백으로 하고, 나머지는 '#'으로 추가
'''
def solution(n, arr1, arr2):    
    map1, map2 = [], []
    for i in range(len(arr1)):
        a = bin(arr1[i])[2:]
        if len(a) != n:
            temp = '0' * (n-len(a))
            a = temp + a
        map1.append(a)
        
    for i in range(len(arr2)):
        b = bin(arr2[i])[2:]
        if len(b) != n:
            temp = '0' * (n-len(b))
            b = temp + b
        map2.append(b)
    
    converged = []
    for i in range(len(map1)):
        row = ''
        for j in range(len(map1[i])):
            if map1[i][j] == '0' and map2[i][j] == '0':
                row += ' '
            else:
                row += '#'
        converged.append(row)

    return converged
