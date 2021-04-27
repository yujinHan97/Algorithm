'''
    알고리즘:
    1. 문제의 요구 그대로 구현하면 된다
'''
def solution(x):
    answer = True
    
    total = 0
    num = x
    while num != 0:
        total += (num % 10)
        num //= 10
                
    if x % total != 0:
        answer = False
        
    return answer

'''
다른 풀이 : 입력받은 수를 str형태로 바꿔서, 각 문자마다 int로 바꾸면서 합을 구한다
st = str(x)
total = 0
for i in range(len(st)):
    total += int(st[i])
'''
