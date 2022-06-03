'''
    알고리즘: 
    --> [][-1][] 이런 형식 이용해서 가장 위에꺼라는 의미하는것 알아두기!!
    --> 원래는 heapq를(우선순위큐) 이용했지만, 다들 스택을 이용해서 다시 풀었다
    알고리즘:
    1. 줄마다 스택을 만들고, 기존 탑에 있는 것보다 높은 음을 낼 수 있으면 (pret이 크면) 삽입
    2. 기존 탑에 있는 것보다 낮은 음을 내야 한다면 while문 돌리면서 낮아질 때 까지 빼고, 낮은 음을 삽입
'''
# 스택사용
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
line_stack = [[] for _ in range(7)]

count = 0
for _ in range(N):
    line, pret = map(int, input().split())  

    if len(line_stack[line]) == 0:
        line_stack[line].append([line, pret])
        count += 1
    else:
        if line_stack[line][-1][1] < pret:
            line_stack[line].append([line, pret])
            count += 1
        elif line_stack[line][-1][1] > pret:
            # while문 앞조건 빠뜨리지 않기!
            while len(line_stack[line]) != 0 and line_stack[line][-1][1] > pret:
                line_stack[line].pop()
                count += 1

            # if의 앞조건 빠뜨리지 않기!
            if len(line_stack[line]) == 0 or line_stack[line][-1][1] != pret:
                line_stack[line].append([line, pret])
                count += 1

print(count)

# heapq 사용
#import sys, heapq
#input = sys.stdin.readline

#N, P = map(int, input().split())
#heap = [[] for _ in range(N)]

#count = 0
#for _ in range(N):
#    line, pret = map(int, input().split())  

#    if len(heap[line]) == 0:
#        heapq.heappush(heap[line], [-pret, pret])
#        count += 1
#    else:
#        if heap[line][0][1] < pret:
#            heapq.heappush(heap[line], [-pret, pret])            
#            count += 1
#        elif heap[line][0][1] > pret:
#            # while문 앞조건 빠뜨리지 않기!
#            while len(heap[line]) != 0 and heap[line][0][1] > pret:
#                heapq.heappop(heap[line])
#                count += 1

#            # if의 앞조건 빠뜨리지 않기!
#            if len(heap[line]) == 0 or heap[line][0][1] != pret:
#                heapq.heappush(heap[line], [-pret, pret])            
#                count += 1

#print(count)
