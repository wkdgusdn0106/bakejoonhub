n = int(input())
pl = []
ma = []
ze = []
for i in range(n):
    a = int(input())
    if a > 0:
        pl.append(a)
    elif a < 0:
        ma.append(a)
    else:
        ze.append(a)
pl.sort();ma.sort()
cnt = 0
for i in range(len(pl)-1,0,-2):
    if pl[i] == 1 or pl[i-1] == 1:
        cnt += pl[i] + pl[i-1]
    else:
        cnt += pl[i]*pl[i-1]
if len(pl) % 2:
    cnt += pl[0]
for i in range(0,len(ma)-1,2):
    cnt += ma[i]*ma[i+1]
if len(ma) % 2:
    if len(ze) == 0:
        cnt += ma[-1]
print(cnt)
