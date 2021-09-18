'''
    알고리즘:
    1. 최대, 최소 값이 1개인 자기 자신이 준 점수이며, count가 1일때만 평균에서 제외하도록 구현
'''
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
    
def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        student = []
        for j in range(len(scores[i])):
            student.append(scores[j][i])
        
        max_sc = max(student)
        min_sc = min(student)
        
        a = student.count(max_sc)
        b = student.count(min_sc)
       
        for k in range(len(student)):
            if k == i:
                if max_sc == student[k] and a == 1:
                    student.remove(student[k])
                elif min_sc == student[k] and b == 1:
                    student.remove(student[k])
        
        total = 0
        for x in range(len(student)):
            total += student[x]
        avg = total / len(student)

        grade_stu = grade(avg)
        answer += grade_stu
    
    return answer
