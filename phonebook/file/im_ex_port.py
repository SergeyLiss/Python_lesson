#

def Import(pb_list, put):
    list_pb = ['id Имя Фамилия Номер Коммент\n']
    for i in range(len(pb_list)):
        temp = pb_list[i].split(";")
        temp2 = f'{i}'
        for j in range(len(temp)):
            temp2 += ' ' + temp[j]
        list_pb.append(temp2)
    
    file = open(put, "w", encoding="utf-8")
    file.writelines(list_pb)
    file.close()
    pass
