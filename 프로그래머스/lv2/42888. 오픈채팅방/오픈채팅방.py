def solution(record):
    rec_list, rec_dict, answer = [], {}, []
    for i in record:
        rec_list.append(i.split())
    for i in rec_list:
        if i[0]!='Leave':
            rec_dict[i[1]]=i[2]
    for i in rec_list:
        if i[0] == 'Enter':
            answer.append(rec_dict[i[1]]+'님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(rec_dict[i[1]]+'님이 나갔습니다.')
    
    return answer