import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dduck = list(map(int, input().split()))
dduck.sort()

# start를 0으로 안해서 틀렸었음
start, end = 0, dduck[n-1]
h = []
while start <= end:
  mid = (start + end) // 2
  cut = 0

  for length in dduck:
    temp = length - mid
    if temp > 0:
      cut += temp

  if cut >= m:
    h.append(mid)
    start = mid + 1
  else:
    end = mid - 1

print(max(h))
