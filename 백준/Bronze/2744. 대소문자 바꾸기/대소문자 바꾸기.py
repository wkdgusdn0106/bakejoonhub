a = input()
for i in range(len(a)):
    st = ord(a[i])
    if 65 <= st <= 90:
        print(chr(st+32),end='')
    else:
        print(chr(st-32),end='')
