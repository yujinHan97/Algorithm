'''
    3273 두 수의 합
    알고리즘:
    1. 투포인터(left, right)를 이용해보았다
    2. 리스트 정렬 후, 리스트의 왼쪽부터 left가 이동
       - 두 개의 포인터의 합이 x랑 같으면, count 수 증가
       - 두 개의 포인터의 합이 x보다 크면, 더 작은 수를 더해야 하니까, right를 이동
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
left = 0 
right = n-1
count = 0

while left < right:
    if a[left] + a[right] == x:
        count += 1
    elif a[left] + a[right] > x:
        right -= 1 
        continue #오른쪽을 옮겼으므로, 왼쪽은 옮기지 않게 하기 위해서 continue

    left += 1

print(count)
