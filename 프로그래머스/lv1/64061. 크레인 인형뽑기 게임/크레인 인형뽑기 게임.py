def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
    
            if board[j][i-1]!=0:
                print("--i,j={},{},{}--".format(j,i-1,board[j][i-1]))
                basket.append(board[j][i-1])
                board[j][i-1]=0
                break

        if len(basket)>=2 :
            if (basket[-1] == basket[-2]):
                answer = answer+2
                print(basket)
                del basket[-2:]
                print(basket)
    return answer