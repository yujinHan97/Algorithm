'''
    알고리즘:
    1. phone_number의 길이에 대하여, 앞에는 모두 *로 출력
    2. 뒤의 4글자는 그대로 출력
'''
def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += '*'
        else:
            answer += phone_number[i]
            
    return answer
  
  '''
  다른 풀이:
  return "*" * (len(phone_number)-4) + phone_number[-4:]
  '''
