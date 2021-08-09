'''
    알고리즘:
    1. 폰켓몬의 종류를 사전 자료형으로 만든다
    2. 가져가야할 폰켓몬 수 < 폰켓몬 종류이면, 최댓값은 폰켓몬 수
    3. 가져가야할 폰켓몬 수 > 폰켓몬 종류이면, 최댓값은 폰켓몬 종류
'''
def solution(nums):
    answer = 0
    pick = len(nums) // 2
   
    # 폰켓몬에 대해서 사전 자료형 생성
    pocketmon = {}
    for i in nums:
        if i in pocketmon.keys():
            pocketmon[i] += 1
        else:
            pocketmon[i] = 1

    # 가져가야할 폰켓몬 수 < 폰켓몬 종류이면, 최댓값은 폰켓몬 수
    if pick <= len(pocketmon):
        answer = pick
    # 가져가야할 폰켓몬 수 > 폰켓몬 종류이면, 최댓값은 폰켓몬 종류
    else:
        answer = len(pocketmon)

    return answer
