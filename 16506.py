'''
    알고리즘:
    1. 문제에 적혀진대로 구현하면 된다.
    2. opcode에 관해서는 일단 사전자료형을 만들고 startswith로 판단한다. C가 붙은 경우에는, len을 비교하여 bit 설정
    3. 이 외의 레지스터 번호들은 모두 2진법을 만들어야 하므로, bin()을 사용하여 이진수를 만듦
    (나는 앞의 자리는 0으로 채우기 위해서 길이 차이만큼 temp에 0을 붙였는데, 다른 풀이를 보니 zfill()을 사용하였다.
    zfill(num) : num에 해당하는 자릿수를 만들고, 빈칸 만큼 0을 채워 넣은 문자열을 반환 => "42".zfill(5) -> '00042'
'''
n = int(input())
assembler = {
  "ADD" : "0000",
  "SUB" : "0001",
  "MOV" : "0010",
  "AND" : "0011", 
  "OR" : "0100",
  "NOT" : "0101",
  "MULT" : "0110",
  "LSFTL" : "0111",
  "LSFTR" : "1000",
  "ASFTR" : "1001",
  "RL" : "1010",
  "RR" : "1011"
}
for _ in range(n):
  machine_code = ''
  op, r, a, b = map(str, input().split())
  r, a, b = int(r), int(a), int(b)

  # 0~4번째 bit
  for key in assembler.keys():
    if op.startswith(key):
      machine_code += assembler[key]
      if len(op) == len(key):
        machine_code += '0'
      else:
        machine_code += '1'
      break

  # 5번째 bit 
  machine_code += '0'

  # 6~8번째 bit
  bin_r = bin(r)[2:]
  temp = ''
  for i in range(3-len(bin_r)):
    temp += '0'
  temp += str(bin_r)
  machine_code += temp
  
  # 9~11번째 bit
  bin_a = bin(a)[2:]
  temp = ''
  if bin_a == 0:
    temp = '000'
  else:
    for i in range(3-len(bin_a)):
      temp += '0'
    temp += str(bin_a)
  machine_code += temp
  
  # 12~15번째 bit
  if machine_code[4] == '0':
    bin_b = bin(b)[2:]
    temp = ''
    for i in range(3-len(bin_b)):
      temp += '0'
    temp += str(bin_b)
    machine_code += temp
    machine_code += '0' # 15번 bit는 항상 0
  else:
    bin_c = bin(b)[2:]
    temp = ''
    for i in range(4-len(bin_c)):
      temp += '0'
    temp += str(bin_c)
    machine_code += temp

  print(machine_code)
  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# zfill() 사용 
n = int(input())
assembler = {
  "ADD" : "0000",
  "SUB" : "0001",
  "MOV" : "0010",
  "AND" : "0011", 
  "OR" : "0100",
  "NOT" : "0101",
  "MULT" : "0110",
  "LSFTL" : "0111",
  "LSFTR" : "1000",
  "ASFTR" : "1001",
  "RL" : "1010",
  "RR" : "1011"
}
for _ in range(n):
  machine_code = ''
  op, r, a, b = map(str, input().split())
  r, a, b = int(r), int(a), int(b)

  # 0~4번째 bit
  for key in assembler.keys():
    if op.startswith(key):
      machine_code += assembler[key]
      if len(op) == len(key):
        machine_code += '0'
      else:
        machine_code += '1'
      break

  # 5번째 bit 
  machine_code += '0'

  # 6~8번째 bit
  bin_r = bin(r)[2:].zfill(3)
  machine_code += bin_r
  
  # 9~11번째 bit
  bin_a = bin(a)[2:].zfill(3)
  machine_code += bin_a
  
  # 12~15번째 bit
  if machine_code[4] == '0':
    bin_b = bin(b)[2:].zfill(3)
    machine_code += bin_b
    machine_code += '0' # 15번 bit는 항상 0
  else:
    bin_c = bin(b)[2:].zfill(4)
    machine_code += bin_c

  print(machine_code)
