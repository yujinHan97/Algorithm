'''
    알고리즘:
    (다시풀기, *** 최소힙에서 최대값 삭제하는 방법 ***)
    heapq.nlargest(n, heap) => heap에서 n개의 큰 원소 리스트로 반환(내림차순 되어있음)
    heapq.nsmallest(n, heap) => heap에서 n개의 작은 원소 리스트로 반환(오름차순 되어있음)
    따라서, 최소힙에서 최대값을 삭제하려면?
    1. 힙의 길이만큼 nlargest 반환
    2. 내림차순으로 반환된 것을 index가 1인 것부터만 다시 heap으로 저장
    3. heap으로 새로 저장된 애들을 heapify
'''
import heapq

def solution(operations):
    h = []    
    for operation in operations:
        op = operation[0]
        
        if op == "I":
            num = int(operation[2:])
            heapq.heappush(h, num)    
        else:
            if h and operation[2] == '-':
                heapq.heappop(h)
            elif h and operation[2] != '-':
                # heap의 길이만큼 nlargest 반환 => temp는 내림차순 리스트 형태
                temp = heapq.nlargest(len(h), h)
                # 내림차순으로 반환된 것을 index가 1인 것부터만 다시 heap으로 저장
                h = temp[1:]
                # heap으로 새로 저장된 애들을 heapify
                heapq.heapify(h)
                
    if h:
        min_v = h[0]
        max_v = max(h)
        answer = [max_v, min_v]
    else:
        answer = [0, 0]
        
    return answer
