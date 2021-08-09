'''
    1912 연속합
    알고리즘:
    1. 연속적인 부분 수열의 합이 가장 커야 하므로, 양수와 음수로 기준을 나누었다
    2. 입력받은 수열을 -를 기준으로 연속적으로 양수이면 합한 결과를 넣고, 음수는 그대로 넣는다
    3. 동적계획법을 이용하는데, dp에 앞에서부터 합을 저장한다
    4. 이 때, 수열에서 음수를 만나도 양수이면 계속 더해가는데, 음수를 만나서 음수가 되면 그 다음 수는 처음부터 시작
'''
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))

newarray = []
temp = 0
for i in range(N-1):
    if array[i] >= 0: # 수열의 수가 양수이면서 
        if array[i+1] >= 0: # 그 다음번 수도 양수이면 임의의 변수에 더함
            temp += array[i]
        else: # 그 다음번 수가 음수이면 더한 결과값을 newarray에 넣기
            temp += array[i]
            newarray.append(temp)   
            temp = 0 # 다음에도 더해야 하니까 temp는 0으로 초기화
    elif array[i] < 0: # 수열의 수가 음수이면 newarray에 그냥 넣기
        newarray.append(array[i])
# 마지막 원소들에 대해서도 추가적인 작업 필요
if array[N-1] >= 0:
    temp += array[N-1]
    newarray.append(temp)
else:
    newarray.append(array[N-1])
#print(newarray)

# 동적계획법 이용
dp = [0] * (len(newarray)+1)
for i in range(1, len(newarray)+1):
    if dp[i-1] >= 0: # 이전까지의 합이 양수이면 현재의 수도 더하여 갱신
        dp[i] = dp[i-1] + newarray[i-1]
    else: # 이전까지의 합이 음수이면, 현재의 수로 다시 새롭게 시작
        dp[i] = newarray[i-1]

# dp[0]은 인덱스를 위하여 0을 임의로 삽입한것이므로, [1:]에서 최댓값 찾기
print(max(dp[1:]))