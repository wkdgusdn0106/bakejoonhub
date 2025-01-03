import copy
aa = [list(map(lambda x: False if x == '#' else True,input())) for i in range(10)]
ans = float('inf')
m = []
for j in range(0,1<<10):
    a = copy.deepcopy(aa)
    binary = list(map(int,bin(j)[2:].zfill(10)))
    cnt = 0
    n=[]
    for k in range(10):
        if binary[k]:
            if k > 0:
                a[0][k-1] = not(a[0][k-1])
            if k < 9:
                a[0][k+1] = not(a[0][k+1])
            a[0][k] = not(a[0][k])
            a[1][k] = not(a[1][k])
            cnt+=1
            n.append((k))
    for k in range(1,10):
        for i in range(10):
            if a[k-1][i]:
                a[k-1][i] = False
                a[k][i] = not(a[k][i])
                if i > 0:
                    a[k][i-1] = not(a[k][i-1])
                if i < 9:
                    a[k][i+1] = not(a[k][i+1])
                if k < 9:
                    a[k+1][i] = not(a[k+1][i])
                cnt+=1
                n.append((k,i))
    if True not in a[-1]:
        if ans > cnt:
            m = n
        ans = min(ans,cnt)
print(ans)
