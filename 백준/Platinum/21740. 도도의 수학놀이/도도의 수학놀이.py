n = int(input())
a = list(input().split())
z = {'0':'0', '1':'1','2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
ans = []
for i in a:
    l = ''
    for k in i:
        l+=z[k]
    l = l[::-1]
    ans.append([l,i])
ans.sort(key=lambda x: x[0]*10)
new = ans[-1]
for i in ans:
    if len(i[1]) > len(new[1]):
        new = i
    elif len(i[1]) == len(new[1]):
        if int(i[0]) > int(new[0]):
            new = i
c = 0
for i in ans:
    if c == 0 and i == new:
        print(i[1],end='')
        c = 1
    print(i[1],end='')
