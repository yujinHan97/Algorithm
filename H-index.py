'''
    알고리즘:
    1. 가능한 H-index중 가장 큰 수를 골라야 하니까 그냥 역순 정렬하였다.
    2. index를 젤 큰 값에서 감소시키면서 그 값보다 인용수 많은 걸 센다
    3. 그 count가 index이상이면 바로 return 한다. 그러면 그게 H-index의 최댓값
'''
def solution(citations):    
    citations.sort(reverse = True)
    for index in range(citations[0],-1,-1):
        count = 0
        for temp_index in citations:
            if index <= temp_index:
                count += 1
            
        if count >= index:
            return index
