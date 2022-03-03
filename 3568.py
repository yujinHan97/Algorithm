'''
    알고리즘:
    1. 문자열을 뒤쪽부터 처리하면서, 특수 문자가 나타나면 temp에 뒤집어서 붙이기
    2. 특수 문자가 아니라면, 0부터 해당 인덱스까지 변수니까 temp에 제대로 붙이기
    3. 앞서 입력 받았을 때 분리했던 datatype과 temp를 연결해서 출력
'''
# 입력 이렇게 받을 수도 있다는 것 알기!!
datatype, *vars = input().split()

for var in vars:
  # len-2를 한 이유는, 콤마(,)와 세미콜론(;)을 제외하기 위함
  temp = ''
  for i in range(len(var)-2, -1, -1):
    if var[i] == '*':
      temp += var[i]      
    elif var[i] == ']':
      temp += '['
    elif var[i] == '[':
      temp += ']'
    elif var[i] == '&':
      temp += '&'
    else: 
      temp += ' '
      # 변수는 0~i까지 순서대로 
      temp += var[0:i+1]
      break
  temp += ';'
  
  new_var = datatype + temp
  print(new_var)
