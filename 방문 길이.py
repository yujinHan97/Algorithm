'''
    알고리즘
    1. 같은 길인데 방향이 다른건 고려를 하지 않았다 --> 힌트 보고 알아차림
'''
def solution(dirs):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    x, y, answer = 0, 0, 0
    passed = []

    for dir in dirs:
        if dir == 'U':
            nx = x + dx[0]
            ny = y + dy[0]
        elif dir == 'D':
            nx = x + dx[1]
            ny = y + dy[1]
        elif dir == 'L':
            nx = x + dx[2]
            ny = y + dy[2]
        elif dir == 'R':
            nx = x + dx[3]
            ny = y + dy[3]

        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue

        # 순방향, 역방향 모두 방향은 다르지만 같은 길이라는 것!
        if (x, y, nx, ny) in passed or (nx, ny, x, y) in passed:
            x = nx 
            y = ny
            continue
        else: # 새로운 길이니까 passed에 순방향과 역방향 모두 추가하고, 횟수를 1 증가
            passed.append((x, y, nx, ny))
            passed.append((nx, ny, x, y))
            answer += 1
            x = nx 
            y = ny

    return answer
