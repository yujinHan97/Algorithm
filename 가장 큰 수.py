'''
    가장 큰 수 (다시 풀기)
    알고리즘:
    1. lambda 함수로, x*3을 입력한다
    --> x * 3 : 문자열에 3을 곱해주면 해당문자열을 3개 나열하는 것과 같음
        '333', '303030', '343434', '555', '999'를 key로 넣어주고,
        정렬을 하면 303030 -> 333 -> 343434 -> 555 -> 999가 될 것인데
        reverse=True로 해서 거꾸로 정렬된 결과가 리턴됨.
    2. [0,0,0,0] 을 input으로 넣는다면 '0000'이 리턴되므로 int로 변환해서 '0'으로 바꿔야 한다
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse = True)

    return str(int(''.join(numbers)))
