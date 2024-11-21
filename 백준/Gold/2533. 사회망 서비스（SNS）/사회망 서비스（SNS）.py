import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(lambda x: int(x)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [[0]*2 for i in range(n+1)]
def dfs(node,parent):
    dp[node][0] = 0
    dp[node][1] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0],dp[child][1])
dfs(1,-1)
print(min(dp[1][0],dp[1][1]))
