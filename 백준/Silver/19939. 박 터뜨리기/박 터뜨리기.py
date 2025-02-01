n,k = map(int,input().split())
vari = n-k*(k+1)//2
if vari < 0:
    print(-1)
else:
    if vari%k == 0:
        print(k-1)
    else:
        print(k)
