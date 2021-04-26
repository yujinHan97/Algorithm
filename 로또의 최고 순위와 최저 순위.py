'''
    알고리즘:
    1. 맞은 개수와 0의 개수를 각각 센다
    2. 최소 순위는 맞은 개수로만 순위를 정하는 것이고, 최대 순위는 0으로 된 것도 모두 맞다고 해서 순위를 정한 것이다
'''
def rank(correct):
    if correct == 6:
        rank = 1
    elif correct == 5:
        rank = 2
    elif correct == 4:
        rank = 3
    elif correct == 3:
        rank = 4
    elif correct == 2:
        rank = 5
    else:
        rank = 6
        
    return rank
    
def solution(lottos, win_nums):
    answer = []
    correct_count = 0    
    zero_count = 0
    for i in range(len(win_nums)):
        if lottos[i] == 0:
            zero_count += 1
        else:
            if lottos[i] in win_nums:
                correct_count += 1
                
    low = correct_count
    high = correct_count + zero_count
    
    low_rank = rank(low)
    high_rank = rank(high)
    
    answer.append(high_rank)
    answer.append(low_rank)
           
    return answer
