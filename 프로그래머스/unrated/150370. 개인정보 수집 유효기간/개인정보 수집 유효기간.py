import datetime
from datetime import timedelta

def solution(today, terms, privacies):
    terms_dict = {i.split()[0] :i.split()[1]  for i in  terms}
    a,b,c = map(int,today.split('.'))
    today = datetime.date(a,b,c)
    answer = []
    ind = 1
    for i in privacies:
        
        date,term = i.split()
        priv_term = i[-1]
        m=int(terms_dict[priv_term]) 
        due_y,due_m,due_d = map(int,i[:-1].split('.'))
        due_y = due_y + (due_m+m-1)//12
        due_m = (due_m+m-1)%12+1
        due = datetime.date(due_y, due_m, due_d)
        if (due-today).days <=0:
            # answer.append(privacies.index(i)+1) => 중복될때 못가려
            answer.append(ind)
        ind = ind+1
    return answer