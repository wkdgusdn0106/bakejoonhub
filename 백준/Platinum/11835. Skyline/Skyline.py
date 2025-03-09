a = int(input())
b = list(map(int,input().split()))
def one(i):
    global cnt
    if b[i] > 0:
        cnt += 3*b[i]
        b[i] = 0
def two(i):
    global cnt
    if b[i] > 0 and b[i+1] > 0:
        m = min(b[i],b[i+1])
        cnt += 5*m
        b[i] -= m
        b[i+1] -= m
def three(i):
    global cnt
    if b[i] > 0 and b[i+1] > 0 and b[i+2] > 0 :
        m = min(b[i],b[i+1],b[i+2])
        cnt += 7*m
        b[i] -= m
        b[i+1] -= m
        b[i+2] -= m
cnt = 0
if a == 1:
    print(b[0]*3)
    exit()
elif a == 2:
    two(0)
    one(0)
    one(1)
    print(cnt)
    exit()
for j in range(a-2):
    if b[j+1] > b[j+2]:
        mi = min(b[j],b[j+1]-b[j+2])
        b[j]-=mi
        b[j+1]-=mi
        three(j)
        two(j)
        one(j)
        cnt += 5*mi
    else:
        three(j)
        two(j)
        one(j)
two(a-2)
one(a-2)
one(a-1)
print(cnt)
