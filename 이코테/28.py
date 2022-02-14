'''
    알고리즘:
    1. index > 값 : 오른쪽을 탐색
    2. index < 값 : 왼쪽을 탐색
    이와 같은 방식으로 이진 탐색을 하고, 끝까지 찾을 수 없다면 return -1을 하여 구현
'''
def bin_search(start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == mid:
      return mid
    elif arr[mid] < mid:
      start = mid +1      
    else:
      end = mid -1

  return -1

n = int(input())
arr = list(map(int, input().split()))

print(bin_search(0, n-1))
