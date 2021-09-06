import itertools
def findPrime(num):
    if num <= 1:
        return False
    
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            return False
        else:
            continue
            
    return True
        
def solution(numbers):
    answer = 0
    
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])

    if len(nums) == 1 and findPrime(int(nums[0])):
        answer += 1
        return answer
    
    poss = []
    poss = poss + nums
    for i in range(2, len(nums)+1):
        temp = itertools.permutations(nums, i)
        poss = poss + list(temp)
        
    strnum = []
    for tup in poss:
        msg = ''.join(tup)
        strnum.append(int(msg))         
    strnum = list(set(strnum))
    
    for num in strnum:
        if findPrime(num):
            print(num)
            answer += 1
        
    return answer
