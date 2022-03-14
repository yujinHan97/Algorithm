'''
    알고리즘:
    1. Hamming Distance가 가장 최소가 되기 위해서는, 각 열마다 가장 빈번한 횟수로 나온 알파벳을 s로 택하기
    2. s를 설정하고 행마다 열을 비교하면서 다른 DNA의 개수를 세기
'''
n, m = map(int, input().split())
dna = ['A', 'C', 'G', 'T']

dnas = []
for _ in range(n):
  dnas.append(input())

s = ''
for j in range(m):
  dna_dict = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
  for i in range(n):
    keyy = dnas[i][j]
    dna_dict[keyy] += 1

  temp_key = ''
  temp_value = -1
  for key, value in dna_dict.items():
    if value > temp_value:
      temp_value = value
      temp_key = key
  s += temp_key

count = 0
for j in range(m):
  for i in range(n):
    if dnas[i][j] != s[j]:
      count += 1
      
print(s)
print(count)
