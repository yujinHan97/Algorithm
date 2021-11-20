def solution(n):
    if int(n**0.5) == n**0.5:
        return 1
    # (n - i^2)의 제곱근이 정수라면 개수는 2
    for i in range(1, int(n**0.5) + 1):
        if int((n - i**2)**0.5) == (n - i**2)**0.5:
            return 2
    #(n - i^2 - j^2)의 제곱근이 정수라면 개수는 3
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            if int((n - i**2 - j**2)**0.5) == (n - i**2 - j**2)**0.5:
                return 3
    return 4

n = int(input())
print(solution(n))
