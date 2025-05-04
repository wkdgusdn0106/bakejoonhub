n,k = map(int,input().split())
chess = [list(map(int,input().split())) for i in range(n)]
horse = [list(map(int,input().split())) for i in range(k)]
turn = 0
def go(Y,X,Y1,X1,L):
    stack = []
    zxc = 0
    for i in chess[Y][X][1:]:
        if i == L:
            zxc = 1
        if zxc:
            stack.append(i)
            chess[Y][X] = [chess[Y][X][0]]+[v for v in chess[Y][X][1:] if v != i]
            horse[i-1] = [Y1,X1,horse[i-1][2]]
            continue
    if chess[Y1][X1][0] == 1:
        stack.reverse()
    chess[Y1][X1]+=stack
    if len(chess[Y1][X1]) >= 5:
        print(turn)
        exit()
for i in range(n):
    for j in range(n):
        chess[i][j] = [chess[i][j]]
for i in range(k):
    horse[i][0]-=1
    horse[i][1]-=1
    y,x,d = horse[i]
    chess[y][x].append(i+1)
while turn < 1000: #바꿔
    turn += 1
    for i in range(k):
        y,x,di = horse[i]
        if di == 1: #오른쪽임
            if x+1 < n: #움ㅈ기여도 벽 안넘을때
                if chess[y][x+1][0] == 2:
                    horse[i][2] = 2
                    if 0<x and chess[y][x-1][0] != 2:
                        go(y,x,y,x-1,i+1)
                else:
                    go(y,x,y,x+1,i+1)
            else: #벽 넘으면 방향 바꾸고 앞으로 ㄱ
                horse[i][2] = 2
                if chess[y][x-1][0] == 2:
                    continue
                go(y,x,y,x-1,i+1)
        elif di == 2: #왼 ㅇ
            if 0<x: 
                if chess[y][x-1][0] == 2:
                    horse[i][2] = 1
                    if x+1<n and chess[y][x+1][0] != 2:
                        go(y,x,y,x+1,i+1)
                else:
                    go(y,x,y,x-1,i+1)
            else: 
                horse[i][2] = 1
                if chess[y][x+1][0] == 2:
                    continue
                go(y,x,y,x+1,i+1)
        elif di == 3: #위쪽
            if 0<y: 
                if chess[y-1][x][0] == 2:
                    horse[i][2] = 4
                    if y+1<n and chess[y+1][x][0] != 2:
                        go(y,x,y+1,x,i+1)
                else:
                    go(y,x,y-1,x,i+1)
            else: 
                horse[i][2] = 4
                if chess[y+1][x][0] == 2:
                    continue
                go(y,x,y+1,x,i+1)
        else:
            if y+1<n: 
                if chess[y+1][x][0] == 2:
                    horse[i][2] = 3
                    if 0<y and chess[y-1][x][0] != 2:
                        go(y,x,y-1,x,i+1)
                else:
                    go(y,x,y+1,x,i+1)
            else: 
                horse[i][2] = 3
                if chess[y-1][x][0] == 2:
                    continue
                go(y,x,y-1,x,i+1)
print(-1)
