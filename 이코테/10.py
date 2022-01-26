'''
    알고리즘:
    (못풀어서 풀이 본 문제)
    1. lock을 확장해서 진짜 lock은 가운데로 하고 넓혀서 풀면 계산 수월
    2. 모든 방향마다, key를 완전탐색 하면서 key를 넣어서 모두 1이면 true
    3. key를 넣었다가 모두 1이 아니면 다시 빼기를 반복
'''
def rotate(arr):
    row = len(arr)
    col = len(arr[0])
    result = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            result[j][row-i-1] = arr[i][j]
    
    return result

def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] != 1:
                return False
            
    return True
            
def solution(key, lock):
    m  = len(key)
    n = len(lock)
    
    new_lock = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n): 
            new_lock[i+n][j+n] = lock[i][j]
            
    for rot in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                if check(new_lock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
