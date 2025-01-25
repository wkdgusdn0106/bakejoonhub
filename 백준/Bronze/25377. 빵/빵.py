a = int(input())
ans = float('inf')
for i in range(a):
    b,c = map(int,input().split())
    if b <= c:
        ans = max(ans,c)
print(-1 if ans == float('inf') else ans)