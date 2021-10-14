'''
    알고리즘:
    (해결하지 못해 풀이 봤음)
    1. w,h를 좌표로 표현하면 원점을 지나는 직선이 되는데 w의 배수, h의 배수일 때만 점을 지난다. 
    2. 따라서, gcd를 이용하여 멀쩡한 사각형의 개수를 구함
'''
def get_gcd(a, b):
    if b != 0:
        return get_gcd(b, a%b)
    else:
        return a
    
def solution(w, h):
    if w < h:
        w, h = h, w
    
    gcd = get_gcd(w, h)
    
    return w * h - (w + h - gcd)
