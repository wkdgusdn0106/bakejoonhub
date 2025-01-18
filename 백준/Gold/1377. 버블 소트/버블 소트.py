a = int(input())
b = [[int(input()),i] for i in range(a)]
c = sorted(b)
m = 0
for i in range(a):
    m = max(m,c[i][1]-i)
print(m+1)
