a = int(input())
for i in range(a):
    n = int(input())
    li = [0,0,0,0,0]
    li[0]=n//60
    n%= 60

    if n <= 35:
        if n % 10 > 5:
            li[1] = n // 10 + 1
            li[4] = 10 - n % 10
        else:
            li[1] = n // 10
            li[3] = n % 10
    else:
        li[0] += 1
        if n % 10 >= 5:
            li[2] = 6 - (n//10+1)
            li[4] = 10 - n % 10
        else:
            li[2] = 6 - n // 10
            li[3] = n % 10

    print(*li)

