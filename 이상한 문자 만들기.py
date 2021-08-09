'''
    알고리즘:
    1. enumerate를 쓰면 인덱스와 값을 반환해준다
    2. 인덱스가 짝수면 spell을 대문자로 고치고
    3. 인덱스가 홀수면 spell을 소문자로 고쳐서
    4. 새로운 단어를 만들어 list에 넣어주고 join
'''
def solution(s):
    answer = ''
    
    new_list = []
    new_s = s.split(' ')
    for word in new_s:
        new_word = ""
        for index, spell in enumerate(word):
            if index % 2 == 0:
                new_word += spell.upper()
            else:
                new_word += spell.lower()
        
        new_list.append(new_word)

    answer = ' '.join(new_list)
    return answer
