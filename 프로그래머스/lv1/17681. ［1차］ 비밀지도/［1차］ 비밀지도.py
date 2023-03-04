import math

def solution(n, arr1, arr2):
    ma1 = []
    for i in arr1:
        for j in range(n):
            ma1.append(i//(pow(2,n-1-j)))
            i = i%(pow(2,n-1-j))

    ma2 = []
    for i in arr2:
        for j in range(n):
            ma2.append(int(i//(pow(2,n-1-j))))
            i = i%(pow(2,n-1-j))
            
    answer = []
    for i in range(n):
        arow=""
        for j in range(n):
            if(ma1[i*n+j]==1) or (ma2[i*n+j]==1):
                arow = arow+"#"
            else:
                arow = arow + " "
        answer.append(arow)
    return answer