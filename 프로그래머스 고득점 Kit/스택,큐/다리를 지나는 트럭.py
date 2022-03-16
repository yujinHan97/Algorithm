'''
    알고리즘:
    (예전에도 혼자서 못풀고, 이번에도 혼자서 못풀었다. -> 다시 풀기!)
    1. bridge에 최대 가능 대수 만큼 0으로 초기화하고, 넣을 수 있다면 트럭을 넣고 없다면 0을 넣기
    2. 그래야 길이 만큼 초를 셀 수가 있다.
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0] * bridge_length
    while bridge:
        bridge.pop(0)
        answer += 1
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
