'''
    알고리즘:
    1. 왼쪽 키보드, 오른쪽 키보드를 나누어 거리를 구함
'''
left = ['qwert', 'asdfg', 'zxcv']
right = ['yuiop', 'hjkl', 'bnm']
left_dict = {}
right_dict = {}

for i in range(len(left)):
    for j in range(len(left[i])):
        left_dict[left[i][j]] = (i, j)

for i in range(len(right)):
    for j in range(len(right[i])):
        if right[i][j] == 'b' or right[i][j] == 'n' or right[i][j] == 'm':
            right_dict[right[i][j]] = (i, j)
        else:
            right_dict[right[i][j]] = (i, j+1)
s1, s2 = map(str, input().split())
s = input()

time = 0
left_start = left_dict.get(s1)
right_start = right_dict.get(s2)
for i in range(len(s)):
    if s[i] in left_dict.keys():
        dist = abs(left_start[0] - left_dict.get(s[i])[0]) + abs(left_start[1] - left_dict.get(s[i])[1])
        left_start = left_dict.get(s[i])
    else:
        dist = abs(right_start[0] - right_dict.get(s[i])[0]) + abs(right_start[1] - right_dict.get(s[i])[1])
        right_start = right_dict.get(s[i])
    time += dist

time += len(s)
print(time)
