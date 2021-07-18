def solution(str1, str2):
    A, B = [], []
    answer = 0

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            new_str = str1[i]+str1[i+1]
            A.append(new_str.lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            new_str = str2[i]+str2[i+1]
            B.append(new_str.lower())

    A_dict, B_dict = {}, {}
    for i in range(len(A)):
        if A[i] in A_dict.keys():
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1
    for i in range(len(B)):
        if B[i] in B_dict.keys():
            B_dict[B[i]] += 1
        else:
            B_dict[B[i]] = 1
    
    intersect, union = 0, 0
    for key in A_dict:
        if key in B_dict.keys():
            intersect += min(A_dict[key], B_dict.get(key))
    union = len(A) + len(B) - intersect

    if intersect + union == 0:
        answer = 1
    else:
        answer = intersect / union

    answer = int(answer * 65536)
    
    return answer
