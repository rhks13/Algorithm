import datetime
from datetime import timedelta

def code2list(code):
    code_list = [i for i in code]
    while(1):
        try:
            code_list[code_list.index('#')-1]+='#'
            del code_list[code_list.index('#')]
        except: break
    return code_list

def solution(m, musicinfos):
    max_len = 0
    answer = ''
    for i in musicinfos:
        start,end,title,code = i.split(",")
        st = datetime.timedelta(hours = int(start[:2]), minutes = int(start[3:]))
        en = datetime.timedelta(hours = int(end[:2]), minutes = int(end[3:]))

        run_time=(en-st).seconds//60

        song_list = code2list(code)
        heard_list = code2list(m)
        
        song_time = len(song_list)
        
        run_code = song_list * (run_time//song_time) + song_list[:(run_time % song_time)]
        if " ".join(heard_list)+" " in  " ".join(run_code)+" ":
            if max_len < run_time:
                max_len = run_time
                answer = title
            elif max_len == run_time:
                pass
        
    if answer == '':
        return '(None)'
    else:
        return answer