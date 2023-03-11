def solution(s):
    num_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    keys = list(num_dict.keys())
    for i in keys:
        s = s.replace(i,num_dict[i])
    return int(s)