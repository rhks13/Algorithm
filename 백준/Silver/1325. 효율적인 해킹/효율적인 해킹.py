import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
def findmax(i):
    been = [False for _ in range(N+1)]
    cnt = 1
    queue = deque([i])
    been[i] = True
    while queue:
        cur = queue.popleft()
        for nx in adlist[cur]:
            if not been[nx]:
                been[nx]=True
                cnt +=1
                queue.append(nx)

    return cnt

adlist = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adlist[B].append(A)


realmax=1
result = []


for i in range(1,N+1):
    tempmax=findmax(i)
    if realmax<tempmax:
        realmax = tempmax
        result.clear()
        result.append(i)
    elif realmax == tempmax:
        result.append(i)

print(*result)
