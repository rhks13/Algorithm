import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
#도로의 정보 담아주기


res = []
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    #방문한 것을 체크해주기 위해 1부터 시작
    
    while queue:
        y = queue.popleft()
        if visited[y] == k+1:
        	#방문 체크를 위해 1부터 시작하여 
            #카운트한 거리가 1이 더 더하여짐
            res.append(y)
            continue
        for i in graph[y]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[y]+1
                


bfs(x)
if len(res) == 0:
    print(-1)
else:
    res.sort()
    #오름차순 정렬
    
    for i in res:
        print(i)