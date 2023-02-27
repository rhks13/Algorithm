def solution(common):
    answer = 0
    fir_dis = common[1]-common[0]
    sec_dis = common[2]-common[1]
    #등차수열과 등비수열 구분
    if(fir_dis==sec_dis):
        #등차수열의 경우
        answer = common[-1]+fir_dis
    else:
        ratio = sec_dis/fir_dis
        answer = common[-1]*ratio
    return answer