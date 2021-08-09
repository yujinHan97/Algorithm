'''
    2217 로프
    알고리즘:
    1. 입력받은 로프를 내림차순으로 정렬하면,
    2. 버틸 수 있는 하중은 각 로프중 젤 낮은거 * 로프의 개수
    3. 그 중에서 최대값을 구하면 된다
'''
import sys
N = int(input())
rope = []
for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse = True)

for i in range(N):
    rope[i] = rope[i] * (i+1)

print(max(rope))