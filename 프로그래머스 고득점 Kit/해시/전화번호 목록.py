'''
    알고리즘:
    1. zip으로 각 리스트의 요소를 짝지어서 접두어이면 False 반환
'''
def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
        
    return True
