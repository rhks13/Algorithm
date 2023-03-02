def solution(board):
    answer = 0
    nrow = len(board)
    for i in range(nrow*nrow):
        count=0
        for j in range(9):
            x = (i//nrow)-1+j//3
            y = (i%nrow)-1+j%3
            if((x>=0)&(y>=0)&(x<nrow)&(y<nrow)):
                if (board[x][y] ==1):
                    count = count+1

        if(count==0):
            answer=answer+1

    return answer