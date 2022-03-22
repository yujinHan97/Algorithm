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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    알고리즘:
    1. 최소힙, 최대힙 각각을 사용하여 구현 => 넣고 뺄때 항상 최소힙, 최대힙 동기화 해야함
    2. I일때는 최소힙엔 그대로, 최대힙엔 -를 붙여 넣기
    3. 최댓값을 뺄때는, 최대힙에서 -붙인 값을 저장하고 그 값을 최소힙에서도 빼기
    4. 최솟값을 뺄때는, 최소힙에서 -붙인 값을 저장하고 그 값을 최대힙에서도 빼기
'''
import heapq

def solution(operations):
    answer = []
    
    min_h, max_h = [], []
    for operation in operations:
        op = operation.split()
        
        if op[0] == 'I':
            num = int(op[1])
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
        else:   
            if not min_h:
                continue
            else:
                if op[1] == '-1':
                    num = heapq.heappop(min_h) 
                    # 최대힙에는 해당 값이 -붙어진 상태로 존재하니까
                    max_h.remove(-num)
                else:
                    # pop한 값에 -를 붙이고, 최소힙에서 그 값으로 존재하니까 
                    num = -heapq.heappop(max_h)
                    min_h.remove(num)
                    
    if min_h:
        answer = [-max_h[0], min_h[0]]
    else:
        answer = [0, 0]
        
    return answer
