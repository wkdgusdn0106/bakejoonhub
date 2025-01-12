a = list(input())
cnt = 0
b = []
for i in range(len(a)):
    put = 1
    if a[i] == 'B':
        for j in range(i+1,len(a)):
            if a[j] == 'C':
                cnt += 1
                put = 0
                a[j] = 0
                break
    elif a[i] == 0:
        put = 0
    if put:
        b.append(a[i])
for i in range(len(b)):
    if b[i] == 'A':
        for j in range(i+1,len(b)):
            if b[j] == 'B':
                cnt += 1
                b[j] = 0
                break
print(cnt)
