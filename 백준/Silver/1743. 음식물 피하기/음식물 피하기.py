import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    global count
    if i<=0 or j<=0 or i>N or j>M:
        return 0
    if mat[i][j]==1:
        mat[i][j]=0
        count +=1
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i-1,j)
        return 0
    return 0




N,M,K = map(int, input().split())
mat = [[0 for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    r,c = map(int, input().split())
    mat[r][c] = 1


result = []
for i in range(1,N+1):
    for j in range(1, M+1):
        count = 0
        dfs(i,j)
        result.append(count)

print(max(result))
