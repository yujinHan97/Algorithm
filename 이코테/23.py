'''
    알고리즘:
    1. 정렬 기준이 여러개라면, 순서대로 나열하면 된다.
    2. 어떤건 오름차순, 어떤건 내림차순인 경우라면, 오름차순이 기준이니까 내림차순은 -를 표시하면 된다.
'''
import sys
input = sys.stdin.readline

n = int(input())
st = []
for i in range(n):
  st.append(list(map(str, input().split())))
  st[i][1] = int(st[i][1])
  st[i][2] = int(st[i][2])
  st[i][3] = int(st[i][3])

st.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
  print(st[i][0])
