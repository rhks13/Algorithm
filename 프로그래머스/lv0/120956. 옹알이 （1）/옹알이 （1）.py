def solution(babbling):
    bab = ["aya", "ye", "woo", "ma"]
    bab_list = bab.copy()
    answer = 0
        #단어 두개의 조합
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
            bab_list.append(bab[i]+bab[j])
    #단어 세개 조합
    num_list = [1,2,3,4]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if ((i==j)or(i==k)or(j==k)):
                    continue
                bab_list.append(bab[i]+bab[j]+bab[k])  
    #단어 네개 조합
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if ((i==j)or(i==k)or(j==k)or(i==l)or(k==l)or(j==l)):
                        continue
                    bab_list.append(bab[i]+bab[j]+bab[k]+bab[l])
    
    for i in range(len(babbling)):
        if babbling[i] in bab_list:
            answer = answer+1
    return answer
