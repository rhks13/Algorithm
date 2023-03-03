def solution(lines):
    answer = 0
    abox=[]
    for i in lines:
        box = []
        for  j in range(i[0]+1,i[1]+1):
            box.append(j)
        abox.append(box)

    answer = len((set(abox[0]) & set(abox[1])) | (set(abox[0]) & set(abox[2])) | (set(abox[2]) & set(abox[1])))
    
    return answer