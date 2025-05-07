n,x = map(int,input().split())
a = list(map(int,input().split()))
m = float('inf')
for i in range(n-1):
    m = min(m, a[i]+a[i+1])
print(m*x)