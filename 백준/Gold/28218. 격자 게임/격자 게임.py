n,m,k = map(int,input().split())
pan = [list(input()) for i in range(n)]
q = int(input())
pan[n-1][m-1] = False
if pan[n-1][m-2]  != '#':
    pan[n-1][m-2] = True
if pan[n-2][m-1] != '#':
    pan[n-2][m-1] = True

def diagonal(Y,X):
    now = pan[Y][X]
    for d in range(1,min(Y,X)+1):
        dy = Y-d
        dx = X-d
        if dy < 0 or dx < 0:
            break
        if pan[dy][dx] == '#' or pan[dy][dx] != '.':
            continue
        if (Y-dy)%(k+1)==0:
            pan[dy][dx] = now
        else:
            pan[dy][dx] = not now
for ny in range(n-1,-1,-1):
    for nx in range(m-1,-1,-1):
        if pan[ny][nx] == '#':
            continue
        diagonal(ny,nx)
        if ny > 0 and pan[ny-1][nx] == '.':
            pan[ny-1][nx] = not pan[ny][nx]
        if nx > 0 and pan[ny][nx-1] == '.':
            pan[ny][nx-1] = not pan[ny][nx]
for i in range(q):
    y,x = map(int,input().split())
    z = pan[y-1][x-1]
    if z:
        print('First')
    else:
        print('Second')
