import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(lambda x: int(x) if x.isdigit() else x, input().strip())) for _ in range(n)]
dp = [[-1]*m for i in range(n)]
v = [[0]*m for i in range(n)]
def dfs(y,x):
    if not (0 <= y < n and 0 <= x < m):
        return 0
    if graph[y][x] == 'H':
        return 0
    if v[y][x]:
        print(-1)
        exit(0)
    if dp[y][x] != -1:
        return dp[y][x]
    v[y][x] = 1
    ma = 0
    for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        ny = y + dy*graph[y][x]; nx = x + dx*graph[y][x]
        ma = max(ma, dfs(ny,nx))
    v[y][x] = 0
    dp[y][x] = ma + 1
    return dp[y][x]
print(dfs(0,0))
