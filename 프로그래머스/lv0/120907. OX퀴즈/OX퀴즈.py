def solution(quiz):
    answer = []
    for equ in quiz:
        sp_equ=equ.split(" = ")
        try:
            insu=sp_equ[0].split(" - ")
            if(int(insu[0]) - int(insu[1]) == int(sp_equ[1])):
                answer.append("O")
            else:
                answer.append("X")
        except:
            insu=sp_equ[0].split(" + ")
            if(int(insu[0]) + int(insu[1]) == int(sp_equ[1])):
                answer.append("O")
            else:
                answer.append("X")
    return answer