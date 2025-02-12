a = int(input())
b = list(map(int, input().split()))
d = b[:]

for i in range(a):
    for j in range(i):
        if b[j] < b[i]:
            d[i] = max(d[i], d[j] + b[i])

print(max(d))  