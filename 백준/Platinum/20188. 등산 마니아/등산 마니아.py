import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = {i : [] for i in range(1,n+1)}
gcnt = [0]*(n+1)
lcnt = [0]*(n+1)
for i in range(n-1):
    g1,g2 = map(int,input().split())
    graph[g1].append(g2)
    graph[g2].append(g1)
def dfs(idx,length):
    v[idx] = 1
    lcnt[idx] = length
    for i in graph[idx]:
        if v[i] == 0:
            gcnt[idx] += dfs(i,length+1)
    return gcnt[idx]+1
v = [0]*(n+1)
dfs(1,0)
gcnt[1] = 0
cnt = sum(lcnt)*(n-1)
v = [0]*(n+1)
def dfs1(idx):
    global cnt
    v[idx] = 1
    z = gcnt[idx]
    cnt -= z*(z+1)//2
    for i in graph[idx]:
        if v[i] == 0:
            dfs1(i)
dfs1(1)
print(cnt)
