n, b = map(str, input().split())
b = int(b)

answer = 0
length = len(n)
for i in range(length):
  if n[i].isdigit():
    num = int(n[i]) * (b ** (length-i-1))
  else:
    ascii = ord(n[i]) - ord('A') + 10
    num = ascii * (b ** (length-i-1))
  answer += num

print(answer)
