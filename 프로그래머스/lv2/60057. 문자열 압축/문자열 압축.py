def solution(s):
    answer = 9999999
    if len(s) ==1:
        return 1
    for i in range(1,int(len(s)/2)+1): # i개 단위로 잘라 압출
        temp = []
        fin = ''  
        for j in range(0,len(s),i): #자르는 과정
                try:
                    temp.append(s[j:j+i])
                except:
                    temp.append(s[j:])     
        mul = 1
        key = ''
        temp.append('0')
        for k in range(len(temp)-1):

            if temp[k] == temp[k+1]:
                key = temp[k]  
                mul+=1
            else:
                if mul == 1:
                    fin += temp[k]
                else:
                    fin += str(mul)+key
                    mul=1
                
        if answer > len(fin):
            answer = len(fin)
    return answer
"""
    answer = 9999999
    for i in range(1,int(len(s)/2)+1): # i개 단위로 잘라 압출
        temp = []
        cnt = 0
        token = ''
        fin = ''
        for j in range(0,len(s),i): #자르는 과정
            try:
                temp.append(s[j:j+i])
            except:
                temp.append(s[j:])
        mul = 0
        key = ''
        for k in range(len(temp)-1):
            if temp[k] == temp[k+1]:
                key = temp[k]
                mul+=1
            else:
                if mul == 1:
                    fin += key
                else:
                    fin += str(mul)+key
        if answer > len(fin):
            answer = len(fin)

"""
    