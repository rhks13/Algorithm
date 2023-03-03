def solution(dots):
    for i in range(1,4):
        ind = [1,2,3]
        ind.remove(i)
        [a,b]=ind
        vec1 = [float(dots[0][0]-dots[i][0]),float(dots[0][1]-dots[i][1])]
        vec2 = [float(dots[a][0]-dots[b][0]),float(dots[a][1]-dots[b][1])]
        
        if(abs(vec1[1]/vec1[0])==abs(vec2[1]/vec2[0])): #abs에서 걸리는 케이스 있었음
            return 1
        else:
            continue
    return 0