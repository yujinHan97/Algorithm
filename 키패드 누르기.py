'''
    알고리즘:
    (2,5,8,0을 누를 때 거리를 못 구하겠어서 이 부분은 풀이를 보았다)
    1. 2,5,8,0이라면, 숫자와의 차의 절댓값을 구하고, 그 수를 3으로 나눈 몫 + 나머지로 거리를 구한다
'''
def solution(numbers, hand):
    answer = ''
    
    l, r = 10, 12
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            l = numbers[i]
            answer += 'L'
        elif numbers[i] in [3, 6, 9]:
            r = numbers[i]
            answer += 'R'
        else:
            # 해결하지 못해서 찾아본 부분
            if numbers[i] == 0:
                numbers[i] = 11
                
            l_distance = abs(numbers[i] - l)
            l_distance = (l_distance // 3) + (l_distance % 3)
            r_distance = abs(numbers[i] - r)
            r_distance = (r_distance // 3) + (r_distance % 3)
            
            if l_distance == r_distance:
                if hand == "right":
                    answer += 'R'
                    r = numbers[i]
                else:
                    answer += 'L'
                    l = numbers[i]
            elif l_distance > r_distance:
                answer += 'R'
                r = numbers[i]
            else:
                answer += 'L'
                l = numbers[i]
            
    return answer
