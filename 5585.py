'''
    5585 거스름돈
'''
n = 1000 - int(input())
moneys = [500, 100, 50, 10, 5, 1]
count = 0

for money in moneys:
    count += (n // money)
    n %= money

print(count)