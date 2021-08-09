'''
    1339 단어 수학
    알고리즘: 
    1. 각 알파벳이 자리에 따라 중요도를 갖도록 하고
    2. 중요도를 내림차순 정렬하여 가장 중요도 값이 높은 수에 9, 그다음 8, 그다음 7.. 을 곱하여 값을 구하도록
'''
N = int(input())
words = []
for i in range(N):
    words.append(input())

# 알파벳이 자기 자리 수만큼의 중요도를 갖도록 설정 
# ex) ABA에서, A가 100의 자리, 1의 자리에 있으므로, 101의 중요도를 갖도록 설정
#              B는 10의 자리에 있으므로 10의 중요도를 가짐
alpha = [0 for i in range(26)]
for i in words:
    for j in range(len(i)):
        index = ord(i[j]) - ord('A')
        alpha[index] += (10**(len(i)-j-1))

alpha.sort(reverse = True) # 큰 수부터 차례로 내림차순 정렬
ans = 0
for i in range(9, -1, -1):
    ans += (alpha[9-i] * i) # 큰 수에 해당하는 것 부터 9를 곱하고 8을 곱하고... 그리디알고리즘

print(ans)