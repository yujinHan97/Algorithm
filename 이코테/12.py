'''
    알고리즘:
    1. 삭제하거나 설치할 때 마다 possible 함수 돌려서 확인
    2. 설치할 때는 append로 먼저 설치해보고, possible 함수로 체크 => 가능하지 않으면 다시 제거(pop)
    3. 삭제할 때는 먼저 remove로 제거해보고, possible 함수로 체크 => 가능하지 않으면 다시 추가(append)
'''
def possible(answer):
    for x, y, btype in answer:
        if btype == 0: # 기둥 
            if y == 0 or (x, y, 1) in answer or (x-1, y, 1) in answer or (x, y-1, 0) in answer:
                continue
            return False
        else: # 보 
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x+1, y, 1) in answer and (x-1, y, 1) in answer):
                continue
            return False
        
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, btype, install = frame
        if install == 0: # 삭제
            answer.remove((x, y, btype))
            poss = possible(answer)
            if not poss:
                answer.append((x, y, btype))
        else: # 설치
            answer.append((x, y, btype))
            poss = possible(answer)
            if not poss:
                answer.pop()
        
    answer.sort(key = lambda x:(x[0], x[1], x[2]))
    return answer
