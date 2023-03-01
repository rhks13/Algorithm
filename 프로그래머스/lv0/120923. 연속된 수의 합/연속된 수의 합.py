def solution(num, total):
    answer = []
    if num%2==1:
        for i in range(num//2,0,-1):
            answer.append(total//num-i)
        answer.append(total//num)
        for i in range(1,num//2+1):
            answer.append(total//num+i)
    else:
        for i in range(num//2-1,-1,-1)  :
            answer.append(total//num-i)
        for i in range(1,num//2+1)  :
            answer.append(total//num+i)    
    return answer