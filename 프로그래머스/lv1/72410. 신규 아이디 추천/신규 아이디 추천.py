import re
def solution(new_id):
    text=re.sub('[^a-z0-9\-_.]','',new_id.lower())
    text = re.sub('[.]+','.',text)
    if text[0] == '.' : text = text[1:]
    try:
        if text[-1] == '.' : text = text[:-1] 
    except: pass
    if text=='' : text = 'a'
    if len(text)>=16 : text = text[:15]
    if text[-1] == '.' : text = text[:-1] 
    while(len(text)<3):
        text = text+text[-1] 
    return text