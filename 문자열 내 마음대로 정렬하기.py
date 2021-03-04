def solution(strings, n):
    answer = []
    charAtn = []
    
    strings.sort()
    for i in range(len(strings)):
        charAtn.append((strings[i][n],i))
       
    charAtn.sort(key = lambda x:x[0])
    for i in range(len(charAtn)):
        answer.append(strings[charAtn[i][1]])
    
    return answer
