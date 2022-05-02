'''
    알고리즘:
    1. 모음이 4개 이상 연속될 경우
    2. 자음이 4개 이상 연속될 경우
    3. 같은 알파벳이 3개 이상 연속될 경우
    4. 연속된 알파벳이 3개 이상 올 경우
    위 경우 중 1개라도 해당이 된다면 0, 그 외는 모두 1
    각각의 경우를 one, two, three, four를 False로 초기화 한 후, 각 경우에 해당하면 True로 변환하여 답을 출력
'''
def solution(arr):
  answer = []
  ja = ['a', 'e', 'i', 'o', 'u']
  
  for word in arr:
    mc, jc = 0, 0
    one, two, three, four = False, False, False, False

    # 4번 경우 -> 연속된 알파벳이 3개 이상 올 경우 
    for i in range(len(word) - 2):
      sliced = word[i:i+3]
      
      if ord(sliced[2])-ord(sliced[1]) == 1 and ord(sliced[1])-ord(sliced[0]) == 1:
        four = True
        break
      
    first = word[0]
    if first in ja:
      jc += 1
    else:
      mc += 1

    count = 0
    for i in range(1, len(word)):
      # 3번 경우 -> 같은 알파벳 연속 3개 이상
      if word[i] == word[i-1]:
        count += 1
      else:
        count = 1
      if count >= 3:
        three = True
        break

      # 1번 경우 -> 모음 4개 연속
      if word[i] not in ja:
        if word[i-1] not in ja:
          mc += 1
        else:
          mc = 1
        if mc >= 4:
          one = True
          break
          
      # 2번 경우 -> 자음 4개 연속
      elif word[i] in ja:
        if word[i-1] in ja:
          jc += 1
        else:
          jc = 1
        if jc >= 4:
          two = True
          break

    if one == True or two == True or three == True or four == True:
      answer.append(0)
    else:
      answer.append(1)

  return answer
  
# 0, 0, 0, 0, 1, 0
example = ["cdcdc","abcdf","cbaeio","aaabc","abefk","abcde"]
print(solution(example))
