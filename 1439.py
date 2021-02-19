'''
    1439 뒤집기
    알고리즘:
    1. 입력받은 문자열을 0을 기준으로 분리하고, 1을 기준으로 분리해서 각각 list에 넣는다
    2. 각 리스트의 길이는 숫자를 같게 만들도록 뒤집을 때의 연산 횟수이다
    3. 따라서, 길이가 짧은 리스트를 고르면 된다
'''
s = input()
zerolist = s.split('1') 
onelist = s.split('0')

# 리스트안에 빈 문자열들을 제거하는 방법
zerolist = [v for v in zerolist if v]
onelist = [v for v in onelist if v]

if len(zerolist) > len(onelist):
    count = len(onelist)
else:
    count = len(zerolist)

print(count)