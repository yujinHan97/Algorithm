'''
    알고리즘:
    (틀렸던 이유 : 정렬을 길이순으로 했고, 그 길이를 이용해서 for문 돌면서 접두어 같은지 확인했다... 시간 초과) : 다시 풀기
    1. 정렬을 한다
    2. 정렬을 하고 나서 바로 앞이 뒤의 접두어가 아니면 그 뒤부터는 절대 아니니 확인할 필요가 없다 --> 시간을 줄여주는 요소
'''
def solution(phone_book):
    answer = True
    
    phone_book.sort() 

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
            
    return answer
