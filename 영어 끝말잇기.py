'''
    알고리즘:
    1. 끝말잇기 규칙을 지키지 않은 사람을 발견하면 바로 index 찾아서 break
    2. 계속 게임을 이어나가면, 등장한 단어를 저장하는 said 리스트에 단어 저장
    3. index의 값으로 누군지, 몇 번째 인지 알아내기
'''
def solution(n, words):
    answer = []
    
    said = []
    index = 0
    for i in range(len(words)):
        # 맨 첫번째는 항상 said에 넣기
        if len(said) == 0:
            said.append(words[i])
            continue

        # 끝말잇기를 지키지 않은 경우, 한 글자의 단어인 경우, 이미 등장했던 단어인 경우
        if words[i-1][-1] != words[i][0] or len(words[i]) == 1 or words[i] in said:
            index = i + 1
            break

        said.append(words[i])

    # 아무도 안 걸린 경우
    if index == 0:
        answer.append(0)
        answer.append(0)
        return answer

    # 누군가는 걸린 경우, 번호와 몇 번째 차례인지 
    if index % n == 0:
        answer.append(n)
        answer.append(index // n)
    else:
        answer.append(index % n)
        answer.append(index // n + 1)
    
    return answer
