a = list(input())
acnt = 0
bcnt = 0
ccnt = 0
i = 0
ab = 0
bc =0
for i in range(len(a)):
    if a[i] == 'A':
        acnt += 1
        bcnt = 0
    elif a[i] == 'B':
        bcnt += 1
        if acnt >= bcnt and acnt != 0:
            ab += 1
            mi = min(acnt,bcnt)
            acnt -= mi
            bcnt -= mi
bcnt = 0
for i in range(len(a)):
    if a[i] == 'B':
        bcnt += 1
        ccnt = 0
    elif a[i] == 'C':
        ccnt += 1
        if ccnt <= bcnt and bcnt != 0:
            bc += 1
            mi = min(ccnt,bcnt)
            ccnt -= mi
            bcnt -= mi
print(min(a.count('B'), ab+bc))
