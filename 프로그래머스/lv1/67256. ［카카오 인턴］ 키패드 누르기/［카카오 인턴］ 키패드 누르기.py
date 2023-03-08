
def dis(x,y):
    distan=abs((x-1)//3-(y-1)//3)+abs((x-1)%3-(y-1)%3)
    return distan

def solution(numbers, hand):
    result = ''
    h = 'L' if hand == "left" else 'R'
    
    l_key = [1,4,7]
    r_key = [3,6,9]

    l_loc = 10
    r_loc = 12
    
    for i in numbers:
        if i ==0 : i=11
        if i in l_key:
            result = result + 'L'
        elif i in r_key:
            result = result + 'R'
        else:
            if(dis(i,l_loc)==dis(i,r_loc)):
                result = result + h
            else:
                longer = 'L' if dis(i,l_loc) <= dis(i, r_loc) else 'R'
                result = result + longer
                
        if result[-1]=='L':
            l_loc = i
        else:
            r_loc = i
    return result