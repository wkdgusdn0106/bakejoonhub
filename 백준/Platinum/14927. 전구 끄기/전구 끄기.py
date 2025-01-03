z = int(input())
aa = [list(map(int,input().split())) for i in range(z)]
ans = float('inf')
m = []
for j in range(0,1<<z):
    a = [row[:] for row in aa]
    binary = list(map(int,bin(j)[2:].zfill(z)))
    cnt = 0
    n=[]
    for k in range(z):
        if binary[k]:
            if k > 0:
                a[0][k-1] ^= 1
            if k < z-1:
                a[0][k+1] ^= 1
            a[0][k] ^= 1
            a[1][k] ^= 1
            cnt+=1
            n.append((k))
    for k in range(1,z):
        for i in range(z):
            if a[k-1][i]:
                a[k-1][i] ^= 1
                a[k][i] ^= 1
                if i > 0:
                    a[k][i-1] ^= 1
                if i < z-1:
                    a[k][i+1] ^= 1
                if k < z-1:
                    a[k+1][i] ^= 1
                cnt+=1
                n.append((k,i))
    if True not in a[-1]:
        if ans > cnt:
            m = n
        ans = min(ans,cnt)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
