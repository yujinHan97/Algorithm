'''
    오픈 채팅방
    알고리즘:
    1. record를 읽으면서 딕셔너리로 만든다 (split()으로 명령어 구분)
    2. enter일 때는 딕셔너리에 넣고, change일 때는 딕셔너리를 수정
    3. 딕셔너리 다 완성하면, record읽으면서 enter, leave에 해당하는 메시지 출력
'''
def solution(record):
    answer = []
    
    rec_dict = {}
    for i in range(len(record)):
        temp = list(record[i].split())

        if temp[0] == 'Enter' or temp[0] == 'Change':
            rec_dict[temp[1]] = temp[2]

    for i in range(len(record)):
        temp = list(record[i].split())

        if temp[0] == 'Enter':
            msg = rec_dict[temp[1]] + "님이 들어왔습니다."
            answer.append(msg)
        elif temp[0] == 'Leave':
            msg = rec_dict[temp[1]] + "님이 나갔습니다."
            answer.append(msg)
        
    return answer
