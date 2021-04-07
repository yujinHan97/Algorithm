'''
    1644 소수의 연속합
    알고리즘:
    1. 일단 N의 소수 리스트를 만든다
    2. 그 소수 리스트에서 연속된 합을 구하는데, 투포인터를 사용한다
    3. end를 가능한 만큼 이동하면서, 합이 N과 같으면 count 세어준다
    4. 그리고 이전 원소는 sum에서 뺀다
'''
def sosu(N):
    is_sosu = [True] * (N+1)
    m = int(N**0.5)

    for i in range(2, m+1):
        if is_sosu[i] == True:
            for j in range(2*i, N+1, i):
                is_sosu[j] = False

    arr = []
    for i in range(2, N+1):
        if is_sosu[i] == True:
            arr.append(i)

    return arr

N = int(input())
arr = sosu(N)

# 투포인터 이용
end = sum = count = 0
for start in range(len(arr)):
    while sum < N and end < len(arr): # end를 가능한 만큼 이동하면서 더해준다
        sum += arr[end]
        end += 1
        
    if sum == N:
        count += 1
        
    sum -= arr[start] # start부터 end까지 세었으니까 또다른 start부터 시작하기 위해서 방금의 start값은 뺀다

print(count)
