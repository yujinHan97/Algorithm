'''
    생각해내지 못해서 풀이 보고 푼 문제 => 다시 풀기
'''
def solution(word):
    answer = 0
    
    d = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    arr = [781, 156, 31, 6, 1]
    for idx, w in enumerate(word):
        answer += d[w]*arr[idx] + 1

    return answer
    
