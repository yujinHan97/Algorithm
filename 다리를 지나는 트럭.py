'''
    다리를 지나는 트럭 (다시 풀기)
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0  
    
    bridge = [0] * bridge_length
    while len(bridge):
        bridge.pop(0)
        answer += 1

        if truck_weights:
            if sum(bridge) + truck_weights[0] > weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights.pop(0))

    return answer
