import sys
input =sys.stdin.readline

shihyuk = [0, 0] + [1] * 1999
for nohive in range(2, int(2001**0.5)+1):
    if shihyuk[nohive]:
        for fromis_9 in range(nohive **2, 2001, nohive):
            shihyuk[fromis_9] = 0
baekjiheon = set(beautiful for beautiful in range(2001) if shihyuk[beautiful])


n = int(input())
a = list(map(int,input().split()))
ans = []
who = a.pop(0)

def dfs(node):
    idx = a.index(node)
    if v[idx]:
        return 0
    v[idx] = 1
    for k in a:
        if (node+k) in baekjiheon and (k not in match or dfs(match[k])):
            match[k] = node
            return 1
    return 0
for i in range(n-1):
    what = a.pop(0)
    match = {}
    if (who + what) in baekjiheon:
        for j in a:
            v = [0]*(n-2)
            dfs(j)
        if len(match) == n-2:
            ans.append(what)
    a.append(what)
if ans == []:
    print(-1)
else:
    print(*sorted(ans))
