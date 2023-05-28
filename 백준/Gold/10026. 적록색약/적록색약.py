import sys
sys.setrecursionlimit(10**6)

def dfs(i,j,color):
    if i<0 or j<0 or i>=N or j>=N:
        return 0
    if color == mat[i][j] and been[i][j]==False:
        been[i][j]=True
        dfs(i+1,j,color)
        dfs(i-1,j,color)
        dfs(i,j+1,color)
        dfs(i,j-1,color)
    else:
        return 0

def rgdfs(i,j,color):
    if i<0 or j<0 or i>=N or j>=N:
        return 0
    if color == rgmat[i][j] and been[i][j]==False:
        been[i][j]=True
        rgdfs(i+1,j,color)
        rgdfs(i-1,j,color)
        rgdfs(i,j+1,color)
        rgdfs(i,j-1,color)
    else:
        return 0



N = int(input())
mat = []
for i in range(N):
    temp=" ".join(input()).split()
    mat.append(temp)
been = [[False for _ in range(N)] for _ in range(N)]
rgmat = [['B' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if mat[i][j]=='G':
            rgmat[i][j] = 'R'
        else:
            rgmat[i][j] = mat[i][j]

count = 0
RGcount = 0

for i in range(N):
    for j in range(N):
        if been[i][j]==False:
            count +=1
            color = mat[i][j]
            dfs(i,j,color)

been = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if been[i][j]==False:
            RGcount +=1
            color = rgmat[i][j]
            rgdfs(i,j,color)

print(count, end=' ')
print(RGcount)