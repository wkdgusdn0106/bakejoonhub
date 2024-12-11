n = int(input())
a = list(zip(list(map(int,input().split())),[i for i in range(n)]))
a.sort()
a = [[i, a[i][1]] for i in range(n)]
for i in range(n):
    a[i][0] = i
a.sort(key=lambda x: x[1])
for i in a:
    print(i[0],end=' ')
