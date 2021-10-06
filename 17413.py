''' 
    알고리즘:
    1. tag일 때는 flag를 걸어서 제대로 출력
    2. tag가 아닌 건 [::-1]로 역순으로 출력
'''
s = input()
result, temp, isTag = "", "", False

for i in range(len(s)):
    if s[i] == '<':
        result += s[i]
        isTag = True
        continue

    elif s[i] == '>':
        result += temp
        result += s[i]
        temp = ""
        isTag = False
        continue
    
    elif s[i] == ' ':
        if isTag:
            temp += s[i]
        else:
            temp = temp[::-1]
            result += temp
            result += ' '
            temp = ""
    else:
        temp += s[i]

        if i == len(s)-1:
            temp = temp[::-1]
            result += temp
        elif s[i+1] == '<':
            temp = temp[::-1]
            result += temp
            temp = ""

print(result)
