'''
    알고리즘:
    1. 각 단계마다 요구하는 조건 수행하기
'''
def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if i.isdigit() or i.isalpha() or i == '-' or i == '.' or i == '_':
            continue
        else:
            new_id = new_id.replace(i, '')

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계
    new_id = new_id.strip('.')

    # 5단계
    if new_id == "":
        new_id += 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += (new_id[len(new_id) - 1])
    print(new_id)

    answer += new_id
    return answer
