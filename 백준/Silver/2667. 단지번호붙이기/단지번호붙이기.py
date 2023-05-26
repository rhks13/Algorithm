def dfs(i,j):
    global count
    if i>=N or j>=N or j<0 or i <0:
        return 0
    if mat[i][j]==1:
        count +=1
        mat[i][j]=0
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i-1,j)
        return 0
    return 0

N = int(input())
mat = []
for i in range(N):
    temp = list(map(int, " ".join(input()).split()))
    mat.append(temp)

num = 0
result = []
for i in range(N):
    for j in range(N):
        count = 0
        if mat[i][j]==1:
            dfs(i,j)   
            num+=1
            result.append(count)
result = sorted(result)
print(num)
for i in range(len(result)):
    print(result[i])
