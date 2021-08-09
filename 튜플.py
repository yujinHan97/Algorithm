def solution(s):
    s = s[1:len(s)-1]
    temp, count = 0, 1
    nums = []
    num_arr = []
    answer = []
    
    for i in range(len(s)):
        if s[i] == '{' or s[i] == ',':
            continue

        elif s[i].isdigit():
            temp = 10 * temp + int(s[i])
            if s[i+1] == ',':
                nums.append(temp)
                count += 1
                temp = 0
                continue

        elif s[i] == '}':
            nums.append(temp)
            num_arr.append((nums, count))
            temp, count = 0, 1
            nums = []
    
    num_arr.sort(key = lambda x:(x[1]))

    for i in range(len(num_arr)):
        numbers = num_arr[i][0]
    
        for a in numbers:
            if a not in answer:
                answer.append(a)
    
    return answer
