''' 
    4796 캠핑
'''
index = 0
while True:
    L, P, V = map(int, input().split())
    count = 0

    if L == 0 and P == 0 and V == 0:
        break

    count += ((V // P) * L)
    if V % P < L:
        count += (V % P)
    else:
        count += L
    
    index += 1
    print("Case %d: %d"%(index, count))