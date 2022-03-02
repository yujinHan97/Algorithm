'''
    알고리즘:
    1. n이 10만명이니까, O(n^2)은 시간초과 위험이 있으므로 completion으로 dict 자료형 생성
    2. 동명이인이 있을 수 있으므로 완주한 사람 list에서 참가사 사람을 찾을 때 -1 씩 진행
    3. 만약 음수가 된다면, 그건 완주하지 못한 사람을 의미
'''
def solution(participant, completion):    
    comp_dict = {}
    for comp in completion:
        if comp in comp_dict.keys():
            comp_dict[comp] += 1
        else:
            comp_dict[comp] = 1
    
    for part in participant:
        if part not in comp_dict.keys():
            return part
        
        if comp_dict[part] >= 1:
            comp_dict[part] -= 1
        else: # 음수가 되어버리면 완주하지 못한 사람임
            return part
    
