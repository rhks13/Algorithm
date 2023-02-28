def solution(array):
    #중복제거
    ar_set = list(set(array))
    if len(ar_set)==1:
        return ar_set[0]
    #중복 제거된 원소들이 array에 각각 몇개 있는지 확인
    ar_count=[]
    for i in range(len(ar_set)):
        count = 0
        for j in range(len(array)):
            if(ar_set[i]==array[j]):
                count = count+1
        ar_count.append(count)
    sort_count = sorted(ar_count)
    if sort_count[-1]==sort_count[-2]:
        return -1
    else:
        return ar_set[ar_count.index(max(ar_count))]
