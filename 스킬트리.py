'''
    알고리즘:
    1. skill들의 순서를 dict 자료형으로 저장
    2. skill_tree를 순회하면서, skill들에 있는건 skill순서를 아닌건 0으로 표시해서 poss에 붙인다
    3. poss의 값들이 0이 아니면, 1씩차이가 나야한다 --> 순서대로 배워야하니깐
'''
def solution(skill, skill_trees):
    answer = 0
    
    # 1단계
    order = {}
    for i in range(len(skill)):
        order[skill[i]] = i+1
    
    for tree in skill_trees:
        poss = []
        can = True
       
        # 2단계
        for i in range(len(tree)):
            if tree[i] in order.keys():
                poss.append(order[tree[i]])
            else:
                 poss.append(0)
        
        # 3단계
        prior = -1
        for j in range(len(poss)):
            if poss[j] == 0:
                continue
            else:
                if 1 not in poss: # skill에 1이 없으면 그건 첫단계부터 안배운 것 --> 할 수 없음
                    can = False
                    break
                    
                if prior == -1:
                    prior = poss[j]
                else:
                    if poss[j] - prior != 1: # 꼭 1차이가 나야하니까 차이가 1이 아니면 False
                        can = False
                        break
                    else:
                        prior = poss[j]
                        
        if can:
            answer += 1
                
    return answer
