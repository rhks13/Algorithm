from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for move in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_x,new_y = x+move[0], y+move[1]
            if new_x <0 or new_y <0 or new_x>=M or new_y>=N:
                continue
            if been[new_y][new_x] == False and mat[new_y][new_x]!=0:
                been[new_y][new_x] = True
                mat[new_y][new_x] = mat[y][x]+1
                queue.append((new_x, new_y))




N,M = map(int, input().split())
been = [[False for _ in range(M)] for _ in range(N)]

mat = []
for i in range(N):
    temp = list(map(int," ".join(input()).split()))
    mat.append(temp)

bfs(0,0)

print(mat[N-1][M-1])