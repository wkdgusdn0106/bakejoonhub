bulb = [list(map(lambda x: x == 'O',input())) for i in range(10)]
ans = float('inf')

for j in range(1<<10):
    bulbs = [row[:] for row in bulb]
    binary = list(map(int,bin(j)[2:].zfill(10)))
    cnt = 0
    
    #첫 번째 줄
    for k in range(10):
        if binary[k]:
            if k > 0:
                bulbs[0][k-1] ^= 1
            if k < 9:
                bulbs[0][k+1] ^= 1
            bulbs[0][k] ^= 1
            bulbs[1][k] ^= 1
            cnt += 1
    
    #그 밑에꺼
    for k in range(1,10):
        for i in range(10):
            if bulbs[k-1][i]:
                bulbs[k-1][i] ^= 1
                bulbs[k][i] ^= 1
                if i > 0:
                    bulbs[k][i-1] ^= 1
                if i < 9:
                    bulbs[k][i+1] ^= 1
                if k < 9:
                    bulbs[k+1][i] ^= 1
                cnt+=1
    if not any(bulbs[-1]):
        ans = min(ans,cnt)
print(ans)
