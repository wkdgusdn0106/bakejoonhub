import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
z = [list(map(int,input().strip())) for i in range(n)]
queue = deque([(0,0,1)])
while queue:
    x,y,cnt = queue.popleft()
    if x == m -1 and y == n-1:
        print(cnt)
        break
    for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if z[ny][nx] == 1:
                z[ny][nx] = -1
                queue.append((nx,ny,cnt+1))
