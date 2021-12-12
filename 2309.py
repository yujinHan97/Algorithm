'''
    알고리즘:
    1. 9명 중 7명의 키가 100 --> 9명 중 2명의 키가 100과 차이나는 만큼이면 그 두명은 가짜 난쟁이임
'''
def find_seven(arr, minus):
    for i in range(8):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == minus:
                return i, j
            
height = []
for i in range(9):
    height.append(int(input()))
    
nine = sum(height)
minus = nine - 100 # 100과 차이나는 만큼
temp_i, temp_j = find_seven(height, minus) # 2명의 난쟁이의 키가 minus와 같으면 그 두명이 가짜 난쟁이
 
real = []
for i in range(9):
    if i == temp_i or i == temp_j:
        continue
    else:
        real.append(height[i])
        
real.sort()
for i in range(7):
    print(real[i])
        
             
