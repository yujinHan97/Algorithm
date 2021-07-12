def solution(files):
    answer = []

    file_list = []
    for file in files:
        head, number, tail = "", "", ""
        num_index_2 = 0
        for index in range(len(file)):
            if file[index].isdigit():
                if head == "":
                    num_index_1 = index
                    head = file[0:num_index_1]
                    number += file[num_index_1:num_index_1+1]
                else:
                    num_index_2 = index
                    number = file[num_index_1:num_index_2+1]
            else:
                if number != "":
                    break
                else:
                    continue

        if index != len(file)-1:
            tail = file[index:len(file)]    
            
        file_list.append((head, number, tail))

    file_list.sort(key = lambda x:(x[0].lower(), int(x[1])))

    for i in file_list:
        new_str = i[0] + i[1] + i[2]
        answer.append(new_str)
    
    return answer
