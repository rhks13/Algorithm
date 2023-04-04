import re

def solution(s):
    answer = []
    s=s.split("},")
    lis=list(map(lambda x:list(map(int,re.sub('{|}','',x).split(','))), s))
    lis.sort(key = lambda x:len(x))
    answer.append(lis[0][0])
    for i in range(1,len(lis)):
        answer.append(list(set(lis[i]).difference(set(answer)))[0])
    return answer