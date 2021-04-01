'''
    2805 나무 자르기
    알고리즘:
    1. 목재절단기의 높이를 이분탐색으로 구한다
    2. 이 때, 상근이가 가져가야할 높이와 잘린 높이가 정확히 일치하지 않는 경우가 있을 수 있으므로, 
       가져갈 수 있을때(자른 높이 >= 가져갈 높이) 와 가져갈 수 없을때(자른 높이 < 가져갈 높이)로 나눈다
    3. 가져갈 수 있을 때의 높이를 저장해 두고, 최종적으로 while문이 끝나면 그 값을 출력 
       (높이를 저장해 두는 이유는 mid가 가져갈 수 없을 때의 mid로 갱신될 수 있기 때문)
'''
import sys
def bin_search(trees, M):
    start = 0
    end = trees[N-1]

    while start <= end:
        mid = (start + end) // 2

        height = 0
        for h in trees:
            if h > mid:
                height += (h-mid)

        # 남거나 같다면, 목재 절단기의 높이를 올려야 가져갈 높이를 줄일 수 있다
        # 부족하다면, 목재 절단기의 높이를 낮춰야 가져갈 높이를 늘릴 수 있다
        if height >= M: # 남거나 같은 경우 ==> 집에 갖고 갈수 있는 경우
            ans = mid # 값을 꼭 저장해놓기!!!!! 
            start = mid + 1
        else: 
            end = mid - 1

    return ans

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort()
print(bin_search(trees, M))
