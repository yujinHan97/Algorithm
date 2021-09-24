'''
    알고리즘:
    1. 언어는 중복되지 않으니까 사전자료형으로 직업군마다 생성
    2. 선호 언어에 있으면 연산해서 결과에 집어넣고 정렬
'''
def solution(table, languages, preference):
    result = []
    for i in range(len(table)):
        temp = list(map(str, table[i].split()))
        
        # 언어마다 점수를 dict로 생성
        lang_dict = {}
        for j in range(1, 6):
            lang_dict[temp[j]] = 6-j
        
        sum = 0
        for j in range(len(languages)):
            if languages[j] in lang_dict.keys():
                sum += (lang_dict[languages[j]] * preference[j]) 
        result.append((temp[0], sum))
        
    result.sort(key = lambda x:(-x[1], x[0]))
    
    return result[0][0]
