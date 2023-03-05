import math
def solution(dartResult):
    num = []
    bonus = []
    score = ""
    for i in dartResult:
        if i in ['S','D','T','*','#']:
            bonus.append(i)
            num.append(score)
            score = ""
        else:
            score = score+i

    temp = []
    for i in range(len(num)):
        if bonus[i]=='S':
            temp.append(int(num[i]))
        elif bonus[i]=='D':
            temp.append(pow(int(num[i]), 2))
        elif bonus[i]=='T' :
            temp.append(pow(int(num[i]), 3))
        elif bonus[i]=='*':
            try:
                temp[-2] = temp[-2]*2
                temp[-1] = temp[-1]*2
            except:
                temp[-1] = temp[-1]*2
        elif bonus[i]=='#':
            temp[-1]=-temp[-1]
    result = sum(temp)    
    return result