'''
    알고리즘:
    1. 기회마다 분리해서, 각 기회마다 나온 값을 더하여 구했다
'''
def solution(dartResult):
    answer = 0
    
    chances = []
    start, index = 0, 0
    for i in range(len(dartResult)-1):
        if not dartResult[i].isdigit() and dartResult[i+1].isdigit():
            index = i+1
            chances.append(dartResult[start:index])
            start = index
    chances.append(dartResult[index:])
    
    result = []
    for k in range(len(chances)):
        temp = 0
        for i in range(len(chances[k])):
            if chances[k][i] == "S":
                temp = int(chances[k][0:i])
            elif chances[k][i] == "D":
                temp = int(chances[k][0:i])
                temp = temp ** 2
            elif chances[k][i] == "T":
                temp = int(chances[k][0:i])
                temp = temp ** 3
                
            if chances[k][i] == "*":
                if k == 0:
                    temp = temp * 2
                else:
                    temp = temp * 2 
                    answer += result[-1] # 이전꺼 *2를 해야하는데, 이미 전에 한번 더했으니까 *2를 할 필요 없이 한번 더 더하면 된다
            elif chances[k][i] == "#":
                temp = -1 * temp
                
        result.append(temp)
               
    for i in result:
        answer += i 
        
    return answer
