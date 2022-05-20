'''
    알고리즘:
    (다시풀기)
    1. 문제에 나와있는대로 순서대로 풀면된다.
    2. 그런데, 좀 헷갈렸다. 다시 풀기
'''
def rotation(d):
    d -= 1
    if d < 0:
        d = 3
    return d

N, M = map(int, input().split())
r, c, d = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
while True:
    maps[r][c] = 2
    nd = d
    check = False # 청소할 방 남아있으면 True

    for _ in range(4):
        nd = rotation(d)
        nr = r + dx[nd]
        nc = c + dy[nd]

        # 왼쪽에 청소 안되어있으면 청소
        if maps[nr][nc] == 0:
            d = nd
            r, c = nr, nc
            check = True
            count += 1
            break
        else:
            d = nd

    if check:
        continue
    
    nr = r - dx[d]
    nc = c - dy[d]

    if maps[nr][nc] == 1:
        break
    else:
        r = nr
        c = nc

print(count)
