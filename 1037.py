''' 
    1037 약수
    알고리즘:
    1. 1과 자기 자신을 제외한 약수가 모두 주어진다면, 그 약수들을 정렬
    2. 정렬한 약수중에서 젤 큰것과 젤 작은것을 곱하면 그 수가 찾고자 하는 수이다
'''
N = int(input())
yaksu = list(map(int, input().split()))
yaksu.sort()

print(yaksu[0]* yaksu[N-1])