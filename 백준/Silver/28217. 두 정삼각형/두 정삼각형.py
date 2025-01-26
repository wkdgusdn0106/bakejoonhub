n = int(input())
a1 = [list(map(int,input().split())) for i in range(n)]
a2 = [list(map(int,input().split())) for i in range(n)]
def chaey(first,second):
    cnt = 0
    for i in range(n):
        for j in range(len(first[i])):
            if first[i][j] != second[i][j]:
                cnt+=1
    return cnt
def change(tri):
    new = [[] for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(len(tri[i])):
            new[j+n-1-i].append(tri[i][j])
    return new
def dae(tri):
    for i in range(len(tri)):
        tri[i] = list(reversed(tri[i]))
    return tri
ans = float('inf')
for i in range(2):
    for j in range(n):
        a1 = change(a1)
        ans = min(ans,chaey(a1,a2))
    a1 = dae(a1)
print(ans)
