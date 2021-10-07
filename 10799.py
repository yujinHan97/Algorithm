'''
    알고리즘:
    1. 처음엔 2중 for문 사용 ==> 데이터 10만개로 시간초과 ==> 이분 탐색 사용
    2. ( 다음에 ) 바로 나오면 레이저니까 인덱스 laser에 저장
    3. 그 외는, 스택에 넣으면서 튜플로 막대의 인덱스 stick에 저장
    4. 스틱의 튜플을 laser에서 이분 탐색해서 인덱스 차이만큼 더한다음에 그렇게 자르면 막대는 +1개로 생기니까 총 개수는 + 1
'''
import bisect 

s = input()
laser, stick, stack, isLaser = [], [], [], False

for i in range(len(s)):
    if s[i] == '(' and s[i+1] == ')': # 앞뒤로 바로 ()이면 레이저니까 laser에 넣고 continue
        laser.append(i)
        isLaser = True
        continue
    else:
        if isLaser:
            isLaser = False
            continue
        elif s[i] == '(':
            stack.append((s[i], i))
        else:
            a, b = stack.pop()
            stick.append((b, i)) # 스택에서 빼내서 길이를 튜플로 stick에 저장

stick.sort(key = lambda x:x[0]) # 이분탐색 위한 정렬
total = 0
for i in range(len(stick)):
    left = bisect.bisect_left(laser, stick[i][0])
    right = bisect.bisect_right(laser, stick[i][1])

    total += (right - left + 1) # laser로 자른 횟수보다 +1의 조각 스틱이 생기므로

print(total)
